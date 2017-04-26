#!/usr/bin/env python3

import time

from characters.hero import Hero
from characters.enemy import Enemy

"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

"""

def main():
    print("""  _    _       _
 | |  | |     (_)
 | |  | |_ __  _  ___  ___  _ __ _ __  ___
 | |  | | '_ \| |/ __|/ _ \| '__| '_ \/ __|
 | |__| | | | | | (__| (_) | |  | | | \__ \\
  \____/|_| |_|_|\___|\___/|_|  |_| |_|___/""")

    time.sleep(1)
    print(""" __   _____
 \ \ / / __|
  \ V /\__ \_
   \_/ |___(_)""")
    time.sleep(1)
    print("""  ______    _      _
 |  ____|  (_)    (_)         _
 | |__ __ _ _ _ __ _  ___ ___(_)
 |  __/ _` | | '__| |/ _ | __|
 | | | (_| | | |  | |  __|__ \\_
 |_|  \__,_|_|_|  |_|\___|___(_)""")
    time.sleep(1.5)
    print("""___ _  _ ____    ____ ____ ____ _  _ ____ _  _ _ _  _ ____
 |  |__| |___    |__/ |___ |    |_/  |  | |\ | | |\ | | __
 |  |  | |___    |  \ |___ |___ | \_ |__| | \| | | \| |__] """)

    time.sleep(2)
    hero = Hero.create()


    waiting = True
    while waiting:
        ans = input("""PIXIE:
        {}, we need your help. You see, it's kind of a long story.
        Basically, there's this bad guy who needs defeating. I'm sure you'll
        figure it out. Well, bye!
        1. Go left
        2. Go right\n""".format(
            hero.name))
        if ans == '1':
            enemy = Enemy('ZombieBob', -500, 4)
            print("You quietly creep down the path, but a zombie ambushes you! You must fight!")
            waiting = False
        elif ans == '2':
            enemy = Enemy()
            print("The cave is damp and smells of goblin urine. You hear a noise behind you, and turn just in time to duck away from a goblin's blow. You must fight!")
            waiting = False
        else:
            print('That is not a valid choice. Try again.')

    while enemy.alive() and hero.alive():
        hero.print_status()
        enemy.print_status()
        print()
        print("What does {} want to do?".format(hero.name))
        print("1. fight enemy")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        inpt = input()
        if inpt == "1":
            hero.attack(enemy)
        elif inpt == "2":
            pass
        elif inpt == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid inpt {}".format(inpt))

        if enemy.alive():
            # Goblin attacks hero
            enemy.attack(hero)

if __name__ == "__main__":
  main()
