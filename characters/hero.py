class Hero (Character):
    def __init__ (self, name='Samwise Gamgee', health=10, power=5):
        super().__init__(name, health, power)
    @classmethod
    def create(cls):
        name = input('What\'s your Hero\'s name?: ')
        return cls(name)
