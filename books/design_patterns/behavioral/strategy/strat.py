
class Strategy(object):
    def do_action(self):
        pass


class Swim(Strategy):
    def do_action(self):
        print("swim around obstacle")


class Jump(Strategy):
    def do_action(self):
        print("jump over obstacle")


class HeadButt(Strategy):
    def do_action(self):
        print("smack obstacle with ur noggin")


class ObstacleCourse(object):
    def __init__(self):
        self.strat = None

    def set_strat(self, strat):
        self.strat = strat

    def overcome(self):
        self.strat.do_action()


if __name__ == "__main__":
    course = ObstacleCourse()

    course.set_strat(Swim())
    course.overcome()

    course.set_strat(Jump())
    course.overcome()

    course.set_strat(HeadButt())
    course.overcome()
