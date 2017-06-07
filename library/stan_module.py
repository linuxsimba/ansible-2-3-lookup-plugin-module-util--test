from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.stan import print_pretty as stan_print

def main():
    module = AnsibleModule(argument_spec=dict())
    module.exit_json(changed=False, msg="%s OH SO PRETTY AND GAY!" % (stan_print()))

if __name__ == '__main__':
    main()

