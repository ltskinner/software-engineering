
class Runway(object):
    def __init__(self, mediator):
        self.atc = mediator
        self.condition = "DRY"

    def set_condition(self, condition):
        self.condition = condition

    def land(self):
        if self.condition == "DRY":
            print("Runway OK to land")
            self.atc.set_land_status(True)
        else:
            print("Runway in poor condition")
            self.atc.set_land_status(False)


class Flight(object):
    def __init__(self, mediator):
        self.atc = mediator

    def land(self):
        if self.atc.ok_to_land():
            print("Landing")
            self.atc.set_land_status(True)
        else:
            print("Holding pattern")


class Mediator(object):
    def __init__(self):
        self.flight = None
        self.runway = None
        self.land = None

    def register_runway(self, runway: Runway):
        self.runway = runway

    def register_flight(self, flight: Flight):
        self.flight = flight

    def set_land_status(self, status):
        self.land = status

    def ok_to_land(self):
        return self.land


if __name__ == "__main__":

    atc = Mediator()

    runway = Runway(atc)
    atc.register_runway(runway)

    boomer800 = Flight(atc)
    atc.register_flight(boomer800)

    runway.set_condition("WET")
    runway.land()
    boomer800.land()

    runway.set_condition("DRY")
    runway.land()
    boomer800.land()
