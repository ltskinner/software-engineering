
class Life(object):
    def __init__(self):
        self.time = None

    def set_time(self, time):
        print(f"Setting time to: {time}")
        self.time = time

    def save_to_memento(self):
        return self.LifeMemento(self.time)

    def restore_from_memento(self, memento):
        saved_time = memento.get_saved_time()
        self.set_time(saved_time)
        print(f"Restored time: {self.time} from memento")

    class LifeMemento(object):
        def __init__(self, time):
            self.time = time

        def get_saved_time(self):
            return self.time


if __name__ == "__main__":
    life = Life()

    life.set_time("400 BC")
    first = life.save_to_memento()

    life.set_time("10 AD")
    life.set_time("2000 AD")

    life.restore_from_memento(first)
