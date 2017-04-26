import time

from items.armor import Armor
# from items.tonic import Tonic
# from items.weapon import Weapon

class Store:
    # If you define a variable in the scope of a class:
    # This is a class variable and you can access it like
    # Store.items => [Tonic, Sword]
    shirt = Armor("A Ragged Tunic", 5, "This tunic has seen better days. It will provide some protection (+2 health).\n")
    items = [shirt]
    def shop(self, hero):
        print("=====================")
        print("Welcome to the store!")
        print("=====================")
        while True:
            print("You have {} coins.".format(hero.coins))
            print("What do you want to do?\n")
            for i in range(len(Store.items)):
                item = Store.items[i]
                print("{}. Buy {} ({} coins) - {}".format(i + 1, item.name, item.cost, item.desc))
            print("10. leave")
            choice = int(input("> "))
            if choice == 10:
                break
            else:
                item = Store.items[choice - 1]
                hero.buy(item)
                time.sleep(2)
                print("Thanks for your business.\n")
