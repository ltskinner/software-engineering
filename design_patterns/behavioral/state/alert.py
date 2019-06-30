
class AlertState():
    def alert(self):
        pass


class Ringer(AlertState):
    def alert(self):
        print("ringing...")


class Vibration(AlertState):
    def alert(self):
        print("vibrating...")


class Silent(AlertState):
    def alert(self):
        print("silent...")


class AlertStateContext(object):
    def __init__(self):
        self.state = None

    def set_state(self, state):
        self.state = state

    def alert(self):
        if self.state is None:
            raise ValueError("Please specify state with set_state()")
        self.state.alert()


if __name__ == "__main__":

    alerter = AlertStateContext()

    alerter.set_state(Silent())
    alerter.alert()

    alerter.set_state(Ringer())
    alerter.alert()
    alerter.alert()
