from random import randint

class Character:
    def __init__(self, name, health, power, coins):
        self.name = name
        self.health = health
        self.power = power
        self.coins = coins

    def attack(self, target):
        crit_dice = randint(0, 10)
        if crit_dice > 6:
            print("Critical hit!")
            target.health -= self.power * 2
        else:
            target.health -= self.power
        print("{} does {} damage to {}.".format(
            self.name, self.power, target.name))
        if target.health <= 0:
            print("{} is dead.".format(target.name))
            print("You loot the corpse and retrieve {} coins".format(
                target.coins))
            self.coins += target.coins

    def alive(self):
        if self.health > 0:
            return True
        else:
            return False

    def print_status(self):
        print("{} has {} health and {} power.".format(self.name, self.health, self.power))
