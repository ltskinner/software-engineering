"""https://www.tutorialspoint.com/python_design_patterns
/python_design_patterns_adapter.htm
"""


class EUSocketInterface(object):
    def voltage(self):
        pass

    def live(self):
        pass

    def neutral(self):
        pass

    def earth(self):
        pass


class Socket(EUSocketInterface):
    """Adaptee class"""
    def voltage(self):
        return 230

    def live(self):
        return 1

    def neutral(self):
        return -1

    def earth(self):
        return 0


class USASocketInterface(object):
    """Target interface"""
    def voltage(self):
        pass

    def live(self):
        pass

    def neutral(self):
        pass


class Adapter(USASocketInterface):
    """Things defined at this level are shared by all object implementations
    """
    def __init__(self, socket):
        self._socket = socket

    def voltage(self):
        return 110

    def live(self):
        return self._socket.live()

    def neutral(self):
        return self._socket.neutral()


class ElectricDevice(object):
    """Client"""
    def __init__(self, power):
        self._power = power

    def boil(self):
        if self._power.voltage() > 110:
            print("TOO MUCH POWER")
        else:
            if self._power.live() == 1 and self._power.neutral() == -1:
                print("we cookin")
            else:
                print("no power")

if __name__ == "__main__":

    socket = Socket()
    adapter = Adapter(socket)

    device = ElectricDevice(adapter)
    device.boil()
