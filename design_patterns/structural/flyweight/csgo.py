
from random import randint


class Player(object):
    def assignWeapon(self, weapon):
        self.weapon = weapon

    def mission(self):
        pass


class CounterTerrorist(Player):
    def __init__(self):
        self.TASK = "DEFUSE THE BOMB, KILL ALL TERRORISTS"

    def mission(self):
        print(f"Asset is to: {self.TASK} with a: {self.weapon}")


class Terrorist(Player):
    def __init__(self,):
        self.TASK = "PLANT A BOMB"
        super().__init__()

    def mission(self):
        print(f"Terrorist is to: {self.TASK} with a: {self.weapon}")


class PlayerFactory(object):
    def __init__(self):
        self.players = {}

    def get_player(self, player_type):
        if player_type in self.players.keys():
            player = self.players[player_type]
        else:
            if player_type.upper() == "ASSET":
                print("New Asset created")
                player = CounterTerrorist()
            elif player_type.upper() == "TERRORIST":
                print("New Terrorist created")
                player = Terrorist()
            else:
                raise ValueError(f"{player_type} is not a valid player")

            self.players[player_type] = player

        return player


class CounterStrike(object):
    def __init__(self, NUM_PLAYERS):
        self.NUM_PLAYERS = NUM_PLAYERS
        self.factory = PlayerFactory()
        self.player_types = ["Asset", "Terrorist"]
        self.weapons = ["M4A1", "M40A5", "Barret", "AK-47"]

    def run(self):
        for _ in range(self.NUM_PLAYERS):
            player_type = self.get_player_type()
            player = self.factory.get_player(player_type)

            weapon_type = self.get_weapon_type()
            player.assignWeapon(weapon_type)

            player.mission()

    def get_player_type(self):
        code = randint(0, len(self.player_types)-1)
        return self.player_types[code]

    def get_weapon_type(self):
        code = randint(0, len(self.weapons)-1)
        return self.weapons[code]


if __name__ == "__main__":
    game = CounterStrike(15)
    game.run()

