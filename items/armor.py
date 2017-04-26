import time

from items.base import Item

class Armor(Item):
    def equip(self, hero):
        print("{}'s health is {}.".format(
            hero.name, hero.health))
        time.sleep(0.3)
        print("{} puts on {}.".format(
            hero.name, self.name))
        time.sleep(0.3)
        print("~ * . . . . * ~")
        time.sleep(0.3)
        hero.health += 2
        print("{}'s health increases to {}!\n\n".format(
            hero.name, hero.health))
