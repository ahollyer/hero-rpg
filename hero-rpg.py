#!/usr/bin/env python3

"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

"""

class Hero:
    def __init__(self, health=10, power=5):
        self.health = health
        self.power = power

class Goblin:
    def __init__(self, health=6, power=2):
        self.health = health
        self.power = power


def main():
    hero = Hero()
    goblin = Goblin()
    # hero.health = 10
    # hero.power = 5
    # goblin.health = 6
    # goblin_power = 2

    while goblin.health > 0 and hero.health > 0:
        print("You have {} health and {} power.".format(hero.health, hero.power))
        print("The goblin has {} health and {} power.".format(goblin.health, goblin.power))
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        inpt = input()
        if inpt == "1":
            # Hero attacks goblin
            goblin.health -= hero.power
            print("You do {} damage to the goblin.".format(hero.power))
            if goblin.health <= 0:
                print("The goblin is dead.")
        elif inpt == "2":
            pass
        elif inpt == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid inpt {}".format(inpt))

        if goblin.health > 0:
            # Goblin attacks hero
            hero.health -= goblin.power
            print("The goblin does {} damage to you.".format(goblin.power))
            if hero.health <= 0:
                print("You are dead.")

if __name__ == "__main__":
  main()
