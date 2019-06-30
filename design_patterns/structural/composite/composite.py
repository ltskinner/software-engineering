
class Equipment(object):
    def __init__(self, name):
        self.name = name

    def power(self):
        pass

    def net_price(self):
        pass

    def add_equipment(self, item):
        pass


class CompositeEquipment(Equipment):
    def __init__(self):
        self.items = []

    def power(self):
        net = 0
        for item in self.items:
            net += item.power()

        return net

    def net_price(self):
        net = 0
        for item in self.items:
            net += item.net_price()

        return net

    def add_equipment(self, item):
        self.items.append(item)


class FloppyDisk(Equipment):
    """Leaf"""
    def __init__(self, name):
        self.name = name

    def power(self):
        return 45

    def net_price(self):
        return 15

    def discount_price(self):
        return 11.5


class Chassis(CompositeEquipment):
    def __init__(self, name):
        self.name = name
        super().__init__()


class Cabinet(CompositeEquipment):
    def __init__(self, name):
        self.name = name
        super().__init__()


if __name__ == "__main__":
    cabinet = Cabinet("cabinet")

    chassis_1 = Chassis("chassis_1")
    chassis_1.add_equipment(FloppyDisk("floppy_1"))
    chassis_1.add_equipment(FloppyDisk("floppy_2"))
    chassis_1.add_equipment(FloppyDisk("floppy_3"))

    cabinet.add_equipment(chassis_1)

    chassis_2 = Chassis("chassis_2")
    chassis_2.add_equipment(FloppyDisk("floppy_4"))

    cabinet.add_equipment(chassis_2)

    print(cabinet.net_price())
