# 在模块加载时，为其添加补丁
# 而且只有当模块加载的时候才这么做

import importlib
import sys
from collections import defaultdict

_post_import_hooks=defaultdict(list)

class PostImportFinder:
    def __init__(self):
        self._skip = set()

    def find_module(self,fullname,path=None):
        print('run find_moduls')
        print(fullname)
        if fullname in self._skip:
            print('skip None')
            return None
        self._skip.add(fullname)
        return PostImportLoader(self)
class PostImportLoader:
    def __init__(self,finder):
        self._finder=finder

    def load_module(self,fullname):
        print('run load_moduls')
        importlib.import_module(fullname)
        module=sys.modules[fullname]
        for func in _post_import_hooks[fullname]:
            func(module)
        self._finder._skip.remove(fullname)
        return module

def when_imported(fullname):
    print('run when_imported')
    def decorate(func):
        print(func)
        if fullname in sys.modules:
            print('dddddd')
            func(sys.modules[fullname])
        else:
            print('SSSS')
            _post_import_hooks[fullname].append(func)
        return func
    print('XXXX')
    return decorate

sys.meta_path.insert(0,PostImportFinder())


@when_imported('threading')
def warn_threads(mod):
    print(mod)
    print('Thread? Are you crazy?')

import threading

