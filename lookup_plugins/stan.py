from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


from ansible.errors import AnsibleError
from ansible.plugins.lookup import LookupBase
from ansible.module_utils.stan import print_pretty as stan_print

class LookupModule(LookupBase):
    def run(self, terms, variables, **kwargs):
        ret = []
        ret.append(stan_print())
        return ret
