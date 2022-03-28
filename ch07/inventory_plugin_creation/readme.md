# Public API inventory

## Command to execute
ansible-inventory -i inventories/plugin.yml --graph --playbook-dir=./

## Directory setup with file contents
Directory:
ansible.cfg
    [defaults]
    inventory_plugins = ./
inventories/plugin.yml
    plugin: publicapis
    validate_certs: False
inventory_plugins/plugin.py
    script

## Example inputs via ENV variables
export PUBLICAPI_URL='https://api.publicapis.org/entries'

## Tower Enviromrent Variables entry
publicapi_url: 'https://api.publicapis.org/entries'
