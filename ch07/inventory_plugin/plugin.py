# bell_topology.py

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
    inventory: bell_topology
    name: API inventory Plugin
    plugin_type: inventory
    author:
      - Sean Sullivan (ssulliva@redhat.com)
    short_description: Creates an inventory from an API
    version_added: "1.0.0"
    description:
        - Creates an inventory from an API
    options:
        validate_certs:
            description: Whether or not to validate the certificates for the topology
            type: bool
            required: True
        dyn_inv_apiurl:
            description: the api address for the topology server in the form http://configdb.tona.stratus.int.bell.ca/api/v1/topology
            type: string
            required: True
            env:
                - name: DYN_INV_APIURL            
        dyn_inv_no_proxy_list:
            description: A list of hosts to use for no proxy settings, example - localhost,127.0.0.1
            type: string
            default: foo
            env:
                - name: DYN_INV_NO_PROXY_LIST            
        full_inventory:
            description: Whether or not to use a single site or get a full inventory
            type: bool
            default: True
            env:
                - name: FULL_INVENTORY            
        site_id:
            description: Site Id for single site.
            type: int
            default: True
            env:
                - name: SITE_ID
    requirements:
        - python >= 3.4
'''

EXAMPLES = r'''
# Only get hosts and groups from site 6
plugin: bell_topology
validate_certs: False
dyn_inv_apiurl: 'https://configdb.tona.stratus.int.bell.ca/api/v1/topology'
dyn_inv_no_proxy_list: 'localhost,127.0.0.1'
full_inventory: False
site_id: 6

# Get all hosts from Topology Database
plugin: bell_topology
validate_certs: False
dyn_inv_apiurl: 'https://configdb.tona.stratus.int.bell.ca/api/v1/topology'
dyn_inv_no_proxy_list: 'localhost,127.0.0.1'
full_inventory: True

# When enviroment variables are declared instead. 
plugin: bell_topology
validate_certs: False
'''

# Ansible internal request utilities
from ansible.module_utils.six.moves.urllib.parse import urljoin
from ansible.module_utils.urls import Request, ConnectionError, urllib_error

from ansible.errors import AnsibleError, AnsibleParserError
from ansible.plugins.inventory import BaseInventoryPlugin, Constructable

import os

try:
    import requests
except ImportError:
    raise AnsibleError("Python requests module is required for this plugin.")


class InventoryModule(BaseInventoryPlugin, Constructable):

    NAME = 'bell_topology'

    def __init__(self):
        super(InventoryModule, self).__init__()

        # from config
        self.validate_certs = None
        self.dyn_inv_apiurl = None
        self.dyn_inv_no_proxy_list = None
        self.session = None
        self.full_inventory = None
        self.site_id = None

        # global attributes
        self._site_list = None
        self._inventory = None
        self._host_list = None

    def query_tors(self, root_group_name):

        os.environ['no_proxy'] = self.dyn_inv_no_proxy_list
        query = self.dyn_inv_apiurl+'/interface-groups'
        r = requests.get(query, timeout=10, verify=False)
        query_result = r.json()

        tor_groups = query_result['result']

        for tor_group in tor_groups:
            query_base = self.dyn_inv_apiurl+'/interface-groups/interface-group/'
            query = query_base + tor_group['interface_group_name']+'?dc_site_id='+str(tor_group['site_id'])
            try:
                r = requests.get(query, timeout=10, verify=False)
                query_result = r.json()

                interfaces = query_result['result']['interfaces']
                ansible_group = tor_group['interface_group_name'] + '_' + str(tor_group['site_id'])

                group_name = self.inventory.add_group(ansible_group)
                self.inventory.add_child(root_group_name, group_name)

                for tor in interfaces:
                    host_name = self.inventory.add_host(tor)
                    self.inventory.add_child(group_name, host_name)

            except Exception:
                pass

        return

    def query_site(self, root_group_name, site_id):

        os.environ['no_proxy'] = self.dyn_inv_no_proxy_list
        query = f"{self.dyn_inv_apiurl}/tors/site/{site_id}?interface_details=yes"
        r = requests.get(query, timeout=10, verify=False)
        query_result = r.json()
        tor_list = query_result['result']

        for tor in tor_list:

            try:
                tor_name = tor['tor_hostname']

                interfaces = tor['interfaces']
                host_name = self.inventory.add_host(tor_name)

                for interface in interfaces:

                    ansible_group = interface['interface_group'] + '_' + str(site_id)

                    group_name = self.inventory.add_group(ansible_group)
                    self.inventory.add_child(root_group_name, group_name)
                    self.inventory.add_child(group_name, host_name)
            except Exception:
                pass
        return

    def verify_file(self, path):
        valid = False
        if super(InventoryModule, self).verify_file(path):
            if path.endswith(('bell_topology.yaml', 'bell_topology.yml')):
                valid = True
            else:
                self.display.vvv('Skipping due to inventory source not ending in "bell_topology.yaml" nor "bell_topology.yml"')
        return valid
        
    def parse(self, inventory, loader, path, cache=True):
        super(InventoryModule, self).parse(inventory, loader, path)
        self._read_config_data(path)

        # Get inputs.
        self.validate_certs = self.get_option("validate_certs")
        self.dyn_inv_apiurl = self.get_option("dyn_inv_apiurl")
        self.dyn_inv_no_proxy_list = self.get_option("dyn_inv_no_proxy_list")
        self.full_inventory = self.get_option("full_inventory")
        self.site_id = self.get_option("site_id")

        if isinstance(self.site_id, str):
            self.site_id = int(self.get_option("site_id"))

        root_group_name = self.inventory.add_group('group_all')
        # raise AnsibleError('error:  {}'.format(tor_list))
        # raise AnsibleParserError('error:  {}'.format(tor_list))

        if self.full_inventory:
            self.query_tors(root_group_name)
        else:
            self.query_site(root_group_name, self.site_id)
