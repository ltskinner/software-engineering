
class Body(object):
    def get_body(self):
        pass


class JeepBody(Body):
    def __init__(self):
        self._body = "jeep"

    def get_body(self):
        return self._body


class AudiBody(Body):
    def __init__(self):
        self._body = "audi"

    def get_body(self):
        return self._body


class Engine(object):
    def __init__(self):
        self.horsepower = 400

    def get_engine(self):
        return self.horsepower


class Wheel(object):
    def get_size(self):
        pass

    def get_tread(self):
        pass


class OffroadWheel(Wheel):
    def __init__(self):
        self._size = 37
        self._tread = "knobby"

    def get_size(self):
        return self._size

    def get_tread(self):
        return self._tread


class RacingWheel(Wheel):
    def __init__(self):
        self._size = 22
        self._tread = "slick"

    def get_size(self):
        return self._size

    def get_tread(self):
        return self._tread
