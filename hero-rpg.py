#!/usr/bin/env python3

"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

"""
import characters

def main():
    hero = characters.Hero.create()


    waiting = True
    while waiting:
        ans = input('You are stumbling through a dark forest. To your left is a zombie-ridden path, and to your right is a cave full of goblins. What do you do?\n1. Turn left\n2. Turn right\n')
        if ans == '1':
            enemy = characters.enemy('ZombieBob', 600, 4)
            print("You quietly creep down the path, but a zombie ambushes you! You must fight!")
            waiting = False
        elif ans == '2':
            enemy = characters.enemy()
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
