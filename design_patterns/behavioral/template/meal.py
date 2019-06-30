
class MakeMeal(object):
    def prepare(self):
        pass

    def cook(self):
        pass

    def eat(self):
        pass

    def go(self):
        self.prepare()
        self.cook()
        self.eat()


class MakeBurrito(MakeMeal):
    def prepare(self):
        print("making a dank rito")

    def cook(self):
        print("warming the rito up")

    def eat(self):
        print("chowing on the rito")


class MakeChili(MakeMeal):
    def prepare(self):
        print("organizing chili components")

    def cook(self):
        print("mixing everything together")

    def eat(self):
        print("devouring a hot bowl")


if __name__ == "__main__":

    meal = MakeChili()
    meal.go()
