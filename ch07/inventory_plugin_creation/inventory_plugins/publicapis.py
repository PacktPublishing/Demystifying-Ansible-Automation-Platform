DOCUMENTATION = r"""
    inventory: publicapis
    plugin_type: inventory
    author:
      - Sean Sullivan (@sean-m-sullivan)
    short_description: Creates an inventory from an API
    version_added: "2.12.3"
    description:
        - Creates an inventory from an API
    options:
        validate_certs:
            description: Whether or not to validate the certificates for the api
            type: bool
            required: True
        publicapi_url:
            description: the api address for the api server in the form https://api.publicapis.org/entries
            type: string
            required: True
            env:
                - name: PUBLICAPI_URL                                  
    requirements:
        - python >= 3.4
"""

EXAMPLES = r"""
plugin: publicapis
validate_certs: False
publicapi_url: 'https://api.publicapis.org/entries'
"""


# Ansible internal request utilities
from ansible.module_utils.urls import Request, ConnectionError, urllib_error

from ansible.errors import AnsibleError, AnsibleParserError
from ansible.plugins.inventory import BaseInventoryPlugin, Constructable

import os

try:
    import requests
except ImportError:
    raise AnsibleError("Python requests module is required for this plugin.")


class InventoryModule(BaseInventoryPlugin, Constructable):

    NAME = "publicapis"

    def __init__(self):
        super(InventoryModule, self).__init__()

        # from config
        self.validate_certs = None
        self.publicapi_url = None
        self.session = None

        self._inventory = None
        self._host_list = None

    def query_entries(self, root_group_name):

        query = self.publicapi_url
        r = requests.get(query, timeout=10, verify=self.validate_certs)
        query_result = r.json()

        entries = query_result["entries"]

        for entry in entries:
            # Get Hostname
            host_name = self.inventory.add_host(entry["API"])

            # If host name is the same as Category append _group
            # Prevents Cannot add a group to itself error.
            if host_name == entry["Category"]:
                group_name = entry["Category"] + '_group'
                self.inventory.add_group(group_name)
            else:
                group_name = self.inventory.add_group(entry["Category"])

            # Add group to root group, and host to group
            self.inventory.add_child(root_group_name, group_name)
            self.inventory.add_child(group_name, host_name)

            # For all other fields create variable, including original Category value
            for field_name in (
                "Description",
                "Auth",
                "HTTPS",
                "Cors",
                "Link",
                "Category",
            ):
                self.inventory.set_variable(host_name, field_name, entry[field_name])
        return

    def verify_file(self, path):
        valid = False
        if super(InventoryModule, self).verify_file(path):
            if path.endswith(("plugin.yaml", "plugin.yml")):
                valid = True
            else:
                self.display.vvv(
                    'Skipping due to inventory source not ending in "plugin.yaml" nor "plugin.yml"'
                )
        return valid

    def parse(self, inventory, loader, path, cache=True):
        super(InventoryModule, self).parse(inventory, loader, path)
        self._read_config_data(path)

        # Get inputs.
        self.validate_certs = self.get_option("validate_certs")
        self.publicapi_url = self.get_option("publicapi_url")

        # Create root group
        root_group_name = self.inventory.add_group("group_all")
        # raise AnsibleError('error:  {}'.format(tor_list))
        # raise AnsibleParserError('error:  {}'.format(tor_list))

        self.query_entries(root_group_name)
