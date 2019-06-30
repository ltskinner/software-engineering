
class CricketData(object):
    def __init__(self, runs, wickets, overs):
        self.runs = runs
        self.wickets = wickets
        self.overs = overs
        self.observers = dict()

    def update_runs(self, runs):
        self.runs = runs

    def update_wickets(self, wickets):
        self.wickets = wickets

    def update_overs(self, overs):
        self.overs = overs

    def add_observer(self, name, observer):
        observer.update(self.runs, self.wickets, self.overs)
        self.observers[name] = observer

    def broadcast(self):
        for name, observer in self.observers.items():
            print("Updating:", name)
            observer.update(self.runs, self.wickets, self.overs)


class ScoreObserver(object):
    def update(self):
        pass

    def display(self):
        pass


class AverageScore(ScoreObserver):
    def __init__(self, PRED_FACTOR=50):
        self.run_rate = None
        self.predicted_score = None
        self.PRED_FACTOR = PRED_FACTOR

    def update(self, runs, wickets, overs):
        if overs == 0:
            self.run_rate = 0
        else:
            self.run_rate = runs/overs

        self.predicted_score = (self.run_rate * self.PRED_FACTOR)
        self.display()

    def display(self):
        print("-- Average Score Display --")
        print("       Run Rate:", self.run_rate)
        print("Predicted Score:", self.predicted_score)


class CurrentScore(ScoreObserver):
    def __init__(self):
        self.runs = None
        self.wickets = None
        self.overs = None

    def update(self, runs, wickets, overs):
        self.runs = runs
        self.wickets = wickets
        self.overs = overs
        self.display()

    def display(self):
        print("-- Current Score Display --")
        print("   Runs:", self.runs)
        print("Wickets:", self.wickets)
        print("  Overs:", self.overs)


if __name__ == "__main__":

    data = CricketData(runs=0,
                       wickets=0,
                       overs=0)

    average_scoreboard = AverageScore()
    data.add_observer("average", average_scoreboard)
    average_scoreboard.display()

    current_scoreboard = CurrentScore()
    data.add_observer("current", current_scoreboard)
    current_scoreboard.display()

    data.update_runs(45)
    data.update_overs(25)
    data.update_wickets(85)

    data.broadcast()
    average_scoreboard.display()
    current_scoreboard.display()
