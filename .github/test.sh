#!/usr/bin/env bash
set -e

# keep track of the last executed command
trap 'last_command=$current_command; current_command=$BASH_COMMAND' DEBUG
# echo an error message before exiting
trap 'echo "\"${last_command}\" command filed with exit code $?."' EXIT

ansible-playbook ../ch01/create_objects_using_role_include_files.yaml
ansible-playbook ../ch01/create_organization_using_module.yml
ansible-playbook ../ch01/create_organization_using_role.yml
ansible-playbook ../ch01/demo.yml
ansible-playbook ../ch01/get_organization_using_api.yml
# ansible-playbook ../ch04/controller/create_user_groups_api.yml
ansible-playbook ../ch04/controller/create_user_groups_module.yml
ansible-playbook ../ch04/controller/create_user_groups_roles.yml
# ansible-playbook ../ch04/hub/create_user_groups_api.yml
# ansible-playbook ../ch04/hub/create_user_groups_module.yml
# ansible-playbook ../ch04/hub/create_user_groups_roles.yml
ansible-playbook ../ch04/settings/aap_settings_api.yml
ansible-playbook ../ch04/settings/aap_settings_module.yml
# ansible-playbook ../ch04/settings/aap_settings_role.yml
# ansible-playbook ../ch05/credentials/credential_type_api.yml
# ansible-playbook ../ch05/credentials/credentials_api.yml
ansible-playbook ../ch05/credentials/credentials_module.yml
ansible-playbook ../ch05/credentials/credentials_role.yml
ansible-playbook ../ch05/credentials/export_credential_types.yml
# ansible-playbook ../ch05/organizations/organizations_api.yml
ansible-playbook ../ch05/organizations/organizations_module.yml
ansible-playbook ../ch05/organizations/organizations_role.yml
ansible-playbook ../ch05/export_import/export.yml
ansible-playbook ../ch05/hub/repos.yml
ansible-playbook ../ch05/hub/publish.yml
# ansible-playbook ../ch06/hub/create_groups_api.yml
ansible-playbook ../ch06/hub/create_groups_module.yml
ansible-playbook ../ch06/hub/create_groups_roles.yml
# ansible-playbook ../ch06/roles/set_role_api.yml
ansible-playbook ../ch06/roles/set_role_using_module.yml
ansible-playbook ../ch06/roles/set_role_with_roles.yml
ansible-playbook ../ch07/inventory_creation/aap_inventory_module.yml
ansible-playbook ../ch07/inventory_creation/aap_inventory_role.yml
ansible-playbook ../ch07/inventory_sources/aap_inventory_module.yml
ansible-playbook ../ch07/inventory_sources/aap_inventory_role.yml
ansible-playbook ../ch08/roles/ee_builder_base.yml
ansible-playbook ../ch09/collection/publish.yml
ansible-playbook ../ch09/collection/repos.yml
ansible-playbook ../ch09/ee/registery_module.yml
ansible-playbook ../ch09/ee/registery_roles.yml
ansible-playbook ../ch09/controller/controller_ee_modules.yml
ansible-playbook ../ch09/controller/controller_ee_roles.yml
ansible-playbook ../ch10/projects/set_project_using_module.yml
ansible-playbook ../ch10/projects/set_project_with_roles.yml
ansible-playbook ../ch10/job_templates/set_job_template_using_module.yml
ansible-playbook ../ch10/job_templates/set_job_template_with_roles.yml
ansible-playbook ../ch10/workflows/set_workflow_using_module.yml
ansible-playbook ../ch10/workflows/set_workflow_with_roles.yml
ansible-playbook ../ch10/workflows/export.yml
