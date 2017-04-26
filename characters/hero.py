from characters.base import Character

class Hero (Character):
    def __init__ (self, name='Samwise Gamgee', health=10, power=5, coins=10):
        super().__init__(name, health, power, coins)

    @classmethod
    def create(cls):
        name = input('What\'s your Hero\'s name?: ')
        return cls(name)

    def buy(self, item):
        if self.coins >= item.cost:
            self.coins -= item.cost
            item.equip(self)
        else:
            print("You can't afford this!")
