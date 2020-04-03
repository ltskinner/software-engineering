
from copy import deepcopy


class Prototype(object):
    def __init__(self):
        self.species = None
        self.loc = None

    def __repr__(self):
        return f"{self.species} at {self.loc}"

    def get_species(self):
        return self.species

    def get_loc(self):
        return self.loc

    def clone(self):
        pass


class Shrub(Prototype):
    def __init__(self):
        self.species = "green shrub"

    def set_loc(self, loc):
        self.loc = loc

    def clone(self,):
        return deepcopy(self)


class Flower(Prototype):
    def __init__(self):
        self.species = "yellow flower"

    def set_loc(self, loc):
        self.loc = loc

    def clone(self):
        return deepcopy(self)


class GardenFactory(object):
    def __init__(self):
        self._shrub = Shrub()
        self._flower = Flower()

    def plant_shrub(self, loc):
        shrub = self._shrub.clone()
        shrub.set_loc(loc)
        return shrub

    def plant_flower(self, loc):
        flower = self._flower.clone()
        flower.set_loc(loc)
        return flower


if __name__ == "__main__":

    garden = GardenFactory()

    flower_1 = garden.plant_flower("northwest corner")
    shrub_1 = garden.plant_shrub("west sidewalk 1")
    shrub_2 = garden.plant_shrub("west sidewalk 2")

    print(flower_1)
    print(shrub_1)
    print(shrub_2)
