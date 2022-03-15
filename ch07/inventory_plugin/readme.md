# Bell Topology MD Testing

## Command to execute
ansible-inventory -i inventories/bell_topology.yml --graph --playbook-dir=./

## Directory setup with file contents
Directory:
ansible.cfg
    [defaults]
    inventory_plugins = ./
inventories/bell_topology.yml
    plugin: bell_topology
    validate_certs: False
inventory_plugins/bell_topology.py
    script

## Example inputs via ENV variables
export FULL_INVENTORY=true
export DYN_INV_NO_PROXY_LIST='localhost,configdb.tona.local.sh'
export DYN_INV_TOPOLOGY_APIURL='https://configdb.tona.local.sh/api/v1/topology'

## Tower Enviromrent Variables entry
DYN_INV_NO_PROXY_LIST: 'localhost,configdb.tona.local.sh'
DYN_INV_TOPOLOGY_APIURL: 'https://configdb.tona.local.sh/api/v1/topology'
FULL_INVENTORY: true


## code for bearer token
https://stackoverflow.com/questions/29931671/making-an-api-call-in-python-with-an-api-that-requires-a-bearer-token
