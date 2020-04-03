
class Vehicle(object):
    def __init__(self):
        self._body = None
        self._engine = None
        self._wheels = []

    def set_body(self, body):
        self._body = body
    
    def set_engine(self, engine):
        self._engine = engine

    def attach_wheel(self, wheel):
        self._wheels.append(wheel)

    def __repr__(self):
        specs = [
            f"Body: {self._body.get_body()}",
            f"Engine hp: {self._engine.get_engine()}",
            f"Tires: {self._wheels[0].get_size()}"
        ]
        return '\n'.join(specs)

