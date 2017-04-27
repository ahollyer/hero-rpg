#!/usr/bin/env python3

"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

"""
from characters import Character, Hero, Enemy, Medic, Fighter, Ninja, Zombie, Goblin

def main():
    heroClass = input('What character would you like to play? \
        \n1. Fighter (Chance to Critical Hit for double damage)\
        \n2. Medic (Chance to heal self when she attacks)\
        \n3. Ninja (High chance to evade attacks, but very low health)\
        \n')
    if heroClass == "1":
        hero = Fighter.create()
    elif heroClass == "2":
        hero = Medic.create()
    elif heroClass == "3":
        hero = Ninja.create()
    else:
        print("Invalid input {}".format(inpt))

    waiting = True
    while waiting:
        ans = input('You are stumbling through a dark forest. To your left is a zombie-ridden path, and to your right is a cave full of goblins. What do you do?\n1. Turn left\n2. Turn right\n')
        if ans == '1':
            enemy = Zombie('ZombieBob', 10, 4, 0, 0)
            print("You quietly creep down the path, but a zombie ambushes you! You must fight!")
            waiting = False
        elif ans == '2':
            enemy = Enemy('Shagrat the Goblin', 10, 3, 0, 5)
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
            print("Invalid input {}".format(inpt))
        enemy.checkLife(hero)
        #The enemy.checkLife function has replaced if Enemy alive loop. The enemy attacks through actions within the checkLife function

if __name__ == "__main__":
  main()
