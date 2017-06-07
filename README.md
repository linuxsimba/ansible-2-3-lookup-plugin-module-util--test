Found a bug with ansible 2.3 and using playbook level module_utils with lookup_plugins.
It doesn't find the playbook level module_utils module.  Only the system level module_utils.

RUN ``ansible-playbook test.yml`` to view the bug
