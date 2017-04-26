from random import randint

class Character:
    def __init__(self, name, health, power):
        self.health = health
        self.power = power
        self.name = name

    def attack(self, target):
        crit_chance = randint(10)
        print(crit_chance)
        target.health -= self.power
        print("{} does {} damage to {}.".format(
            self.name, self.power, target.name))
        if target.health <= 0:
            print("{} is dead.".format(target.name))

    def alive(self):
        if self.health > 0:
            return True
        else:
            return False

    def crit(self):
        target.health -= self.power * 2
        print("Critical hit!")

    def print_status(self):
        print("{} has {} health and {} power.".format(self.name, self.health, self.power))
