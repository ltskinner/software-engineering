
from implementation import WindowsImplementation, LinuxImplementation


class Bridge(object):
    """The Target interface"""
    def __init__(self):
        self._implementation = None

    def find_python_exe(self):
        raise NotImplementedError()


class InterfaceVariant_1(Bridge):
    """Interface utilizing the bridge"""
    def __init__(self, implementation):
        self._implementation = implementation

    def find_python_exe(self):
        print("Do something special here")
        self._implementation.find_python_exe()


class InterfaceVariant_2(Bridge):
    def __init__(self, implementation):
        self._implementation = implementation

    def find_python_exe(self):
        print("More special work")
        self._implementation.find_python_exe()


if __name__ == "__main__":
    windows = WindowsImplementation()
    linux = LinuxImplementation()

    variant_1 = InterfaceVariant_1(windows)
    variant_1.find_python_exe()

    variant_2 = InterfaceVariant_2(linux)
    variant_2.find_python_exe()
