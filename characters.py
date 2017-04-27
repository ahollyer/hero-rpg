from random import randint

class Character:
    def __init__(self, name, health, power, evade, coin):
        self.health = health
        self.power = power
        self.name = name
        self.evade = evade
        self.max_health = health
        self.coin = coin
    def attack(self, target):
        self.special(target) #Specials before attacks
        target.health -= self.power
        print("{} does {} damage to {}.".format(self.name, self.power,
        target.name))
        # if target.health <= 0:
        #     print("{} is dead.".format(target.name))
    def special(self, target):
        pass
    def item(self, health, power): #Item use function
        print('Item Placeholder')
    def heal(self, healHP): #Healing function
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
    def __init__ (self, name, health, power, evade, coin):
        super().__init__(name, health, power, evade, coin)
    @classmethod
    def create(cls):
        name = input('What\'s your Hero\'s name?: ')
        return cls(name)

class Enemy (Character):
    def __init__ (self, name, health, power, evade, coin):
        super().__init__(name, health, power, evade, coin)
    def checkLife(self, target):
        if self.alive():
            if target.evade > 2:
                print('{} evaded the attack from {}!'.format(target.name, self.name))
            else:
                self.attack(target)
        else:
            print("{} is dead.".format(self.name))
            print('{} gathered {} coins from {}\'s corpse'.format(target.name, self.coin, self.name))
            target.coin += self.coin

class Zombie (Enemy):
    def __init__ (self, name, health, power, evade, coin):
        super().__init__(name, health, power, evade, coin)
    def alive(self):
        if self.health < 0:
            print('Z O M B I E S  D O  N O T  D I E')
        return True

class Goblin (Enemy):
    def __init__ (self, name, health, power, evade, coin):
        super().__init__(name, health, power, evade, coin)

class Fighter (Hero):
    def __init__ (self, name, health=200, power=10, evade=0, coin=0):
        super().__init__(name, health, power, evade, coin)
    def special(self, target):
        crit(self, target)

class Medic (Hero):
    def __init__ (self, name, health=600, power=3, evade=0, coin=0):
        super().__init__(name, health, power, evade, coin)
    def special(self, target):
        healAttack(self, target)

class Ninja (Hero):
    def __init__ (self, name, health=600, power=3, evade=0, coin=0):
        super().__init__(name, health, power, evade, coin)
    def special(self, target):
        dodge(self)

def dodge(self):
    self.evade = randint(1,10)

def crit(self, target):
    critChance = randint(1,5)
    if critChance == 5:
        target.health -= self.power
        print("BOOM! Critical hit! {} does {} additional damage to {}.".format(
            self.name, self.power, target.name))

def healAttack(self, target):
    spell = randint(1,5)
    healHP = randint(self.power, self.power+3)
    if spell == 5:
        self.heal(healHP)
