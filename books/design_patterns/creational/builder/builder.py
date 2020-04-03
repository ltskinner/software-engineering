"""https://www.tutorialspoint.com/python_design_patterns/
python_design_patterns_builder.htm
"""

from vehicle import Vehicle
from parts import JeepBody, Engine, OffroadWheel


class Director(object):
    def set_builder(self, builder):
        self._builder = builder

    def make_vehicle(self):
        vehicle = Vehicle()

        # First goes the body
        body = self._builder.get_body()
        vehicle.set_body(body)

        # Then the engine
        engine = self._builder.get_engine()
        vehicle.set_engine(engine)

        # And 4 wheels
        num_wheels = 4
        for _ in range(num_wheels):
            wheel = self._builder.get_wheel()
            vehicle.attach_wheel(wheel)

        return vehicle


class Builder(object):
    def get_body(self):
        pass

    def get_engine(self):
        pass

    def get_wheel(self):
        pass


class JeepBuilder(Builder):
    """This looks factory"""
    def get_body(self):
        return JeepBody()

    def get_engine(self):
        return Engine()

    def get_wheel(self):
        return OffroadWheel()


if __name__ == "__main__":
    director = Director()

    jeep_builder = JeepBuilder()

    director.set_builder(jeep_builder)
    jeep = director.make_vehicle()

    print(jeep)
