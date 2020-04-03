
from copy import deepcopy


class PlantPrototype(object):
    def __init__(self):
        self.species = None
        self.loc = None

    def __repr__(self):
        return f"{self.species} at {self.loc}"

    def set_species(self, species):
        self.species = species

    def set_loc(self, loc):
        self.loc = loc

    def get_species(self):
        return self.species

    def get_loc(self):
        return self.loc

    def clone(self, species, loc):
        plant = deepcopy(self)
        plant.set_species(species)
        plant.set_loc(loc)
        return plant


if __name__ == "__main__":

    plant = PlantPrototype()

    flower_1 = plant.clone("yellow_flower", "northwest corner")
    shrub_1 = plant.clone("green shrub", "west sidewalk 1")
    shrub_2 = plant.clone("green shrub", "west sidewalk 2")

    print(flower_1)
    print(shrub_1)
    print(shrub_2)
