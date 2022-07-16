# Public API inventory

## Command to execute

ansible-inventory -i inventories/plugin.yml --graph --playbook-dir=./

## Directory setup with file contents

Directory:
in the ansible.cfg file

```ini
[defaults]
inventory_plugins = ./
[inventory]
enable_plugins = publicapis, auto
```

in the inventories/plugin.yml

```yml
    plugin: publicapis
    validate_certs: False
```

The python script runs is found at inventory_plugins/plugin.py

## Example inputs via ENV variables

export PUBLICAPI_URL='https://api.publicapis.org/entries'

## Controller Enviromrent Variables entry

publicapi_url: 'https://api.publicapis.org/entries'
