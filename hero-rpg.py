#!/usr/bin/env python3

"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

"""

class Hero:
    def __init__(self, name='Samwise Gamgee', health=10, power=5):
        self.health = health
        self.power = power
        self.name = name
    def attack(self, target):
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

class Goblin:
    def __init__(self, name='Shagrat', health=6, power=2):
        self.health = health
        self.power = power
        self.name = name
    def attack(self, target):
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


def main():
    hero = Hero()
    goblin = Goblin()

    while goblin.alive() and hero.alive():
        print("{} has {} health and {} power.".format(hero.name, hero.health, hero.power))
        print("{} has {} health and {} power.".format(goblin.name, goblin.health, goblin.power))
        print()
        print("What does {} want to do?".format(hero.name))
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        inpt = input()
        if inpt == "1":
            hero.attack(goblin)
        elif inpt == "2":
            pass
        elif inpt == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid inpt {}".format(inpt))

        if goblin.alive():
            # Goblin attacks hero
            goblin.attack(hero)

if __name__ == "__main__":
  main()
