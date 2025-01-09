class Adventurer:
    def __init__(self, name, age, strength, dexterity, constitution, intelligence, wisdom, charisma):
        self.name = name
        self.age = age
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma
        self.charClass = 'Citizen'

    def printStats(self):
        print("Name: " + self.name)
        print("Age: " + str(self.age))
        print("Class: " + str(self.charClass)) 
        print("Strength: " + str(self.strength))
        print("Dexterity: " + str(self.dexterity))
        print("Constitution: " + str(self.constitution))
        print("Intelligence: " + str(self.intelligence))
        print("Wisdom: " + str(self.wisdom))
        print("Charisma: " + str(self.charisma))

class Warrior(Adventurer):
    def __init__(self, name, age, strength, dexterity, constitution, intelligence, wisdom, charisma):
        super().__init__(name, age, strength, dexterity, constitution, intelligence, wisdom, charisma)
        self.charClass = 'Warrior'
        self.skills = []

