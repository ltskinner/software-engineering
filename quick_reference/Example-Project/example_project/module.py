
from .subpackage import sub_module_function


def module_function():
    print('printing from module.py')
    return True


def use_sub_module_function():
    print('accessing submodule')
    sub_module_function()
    return True
