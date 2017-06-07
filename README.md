Found a bug with ansible 2.3 and using playbook level module_utils with lookup_plugins.
It doesn't find the playbook level module_utils module.  Only the system level module_utils.

RUN ``ansible-playbook test.yml`` to view the bug

Bug Output

```
test_lookup_plugin:% ansible-playbook test.yml -v                                                                                                    <master>
No config file found; using defaults
 [WARNING]: Host file not found: /etc/ansible/hosts

 [WARNING]: provided hosts list is empty, only localhost is available


PLAY [localhost] ***************************************************************************************************************************************************************

TASK [Gathering Facts] *********************************************************************************************************************************************************
ok: [localhost]

TASK [test stan playbook module_utils with a custom module] ********************************************************************************************************************
ok: [localhost] => {"changed": false, "msg": "I AM PRETTY OH SO PRETTY AND GAY!"}

TASK [test stan playbook level module_utils with a custom lookup] **************************************************************************************************************
An exception occurred during task execution. To see the full traceback, use -vvv. The error was: ImportError: No module named stan
fatal: [localhost]: FAILED! => {"failed": true, "msg": "Unexpected failure during module execution.", "stdout": ""}
  to retry, use: --limit @/home/skamithi/test_lookup_plugin/test.retry

PLAY RECAP *********************************************************************************************************************************************************************
localhost                  : ok=2    changed=0    unreachable=0    failed=1


```
