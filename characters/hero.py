from characters.base import Character

class Hero (Character):
    def __init__ (self, name='Samwise Gamgee', health=10, power=5):
        super().__init__(name, health, power)
    @classmethod
    def create(cls):
        name = input("""\nPIXIE:
        Welcome to FairyLand! I'm the gumdrop pixie, and I've
        brought you here using sprinkle magic. We've been waiting many
        centuries for a magical unicorn princess like you.\n
        What is your name, princess? """)
        return cls(name)
