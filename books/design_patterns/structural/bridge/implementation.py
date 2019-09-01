
class Implementator(object):
    """Interface for the background implementation"""
    def find_python_exe(self):
        raise NotImplementedError()


class WindowsImplementation(Implementator):
    """Concrete implementation"""
    def find_python_exe(self):
        print("C:/Program Files/python.exe")


class LinuxImplementation(Implementator):
    """Concrete Implementation"""
    def find_python_exe(self):
        print("/usr/python.exe")
