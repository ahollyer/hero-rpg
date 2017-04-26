from random import randint

class Character:
    def __init__(self, name, health, power):
        self.health = health
        self.power = power
        self.name = name
    # def attack(self, target): #Propose removing attack function from main Character class and moving to individual characters
    #     target.health -= self.power
    #     print("{} does {} damage to {}.".format(
    #         self.name, self.power, target.name))
    #     if target.health <= 0:
    #         print("{} is dead.".format(target.name))
    def item(self, health, power): #Item use function
        print('Item Placeholder')
    def heal(self, healHP):
        self.health += healHP
        print('{} heals {} damage!'.format(self.name, healHP))
    def action(self, target):#Placeholder for flexibility to define a Character's actions beyond attack and Do Nothing
        print('Action Placeholder')
    def alive(self):
        if self.health > 0:
            return True
        else:
            return False
    def print_status(self):
        print("{} has {} health and {} power.".format(self.name, self.health, self.power))

class Hero (Character):
    def __init__ (self, name, health=100, power=5):
        super().__init__(name, health, power)
    def result(self, target):
        print('Resultplaceholder')
    @classmethod
    def create(cls):
        #name = input('What\'s your Hero\'s name?: ')
        heroClass = int(input('What character would you like to play? \
            \n1. Steiner the Fighter (Chance to Critical Hit for double damage)\
            \n2. Garnet the Medic (Chance to heal self when she attacks)'))
        return cls(heroClass)

class Enemy (Character):
    def __init__ (self, name = 'Shagrat the goblin', health=6, power=2):
        super().__init__(name, health, power)
    def attack(self, target):
        target.health -= self.power
        print("{} does {} damage to {}.".format(
            self.name, self.power, target.name))
        if target.health <= 0:
            print("{} is dead.".format(target.name))

class Fighter (Hero):
    def __init__ (self, name = 'Steiner the Fighter', health=200, power=10):
        super().__init__(name, health, power)
    def attack(self, target):
        crit = randint(1,5)
        if crit == 5:
            target.health -= self.power*2
            print("BOOM! Critical hit! {} does {} damage to {}.".format(
                self.name, self.power*2, target.name))
        else:
            target.health -= self.power
            print("{} does {} damage to {}.".format(
                self.name, self.power, target.name))

class Medic (Hero):
    def __init__ (self, name = 'Garnet the Medic', health=600, power=3, spellpower=2):
        super().__init__(name, health, power)
    def attack(self, target):
        spell = randint(1,5)
        healHP = randint(self.spellpower, self.spellpower+3)
        if spell == 5:
            self.heal(healHP)
            target.health -= self.power
            print("{} does {} damage to {}!".format(
                self.name, self.power, target.name))
        else:
            target.health -= self.power
            print("{} does {} damage to {}.".format(
                self.name, self.power, target.name))

class Ninja (Character):
    def __init__ (self, name = 'Shadow the Ninja', health=6, power=3):
        super().__init__(name, health, power)
