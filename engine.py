# IMPORTS
# Imports from Python Standard Libraries
import random

# Imports from other python scripts
import adventurer as adv

class Engine:
    def rollDice(sides):
        return random.randrange(1, sides)

    def createRandomCharacter(self, name, charClass = None):
        strength = self.rollDice(20)
        dexterity = self.rollDice(20)
        constitution = self.rollDice(20)
        intelligence = self.rollDice(20)
        wisdom = self.rollDice(20)
        charisma = self.rollDice(20)
        age = self.rollDice(100)
        if charClass == 'Warrior':
            return adv.Warrior(name, age, strength, dexterity, constitution, intelligence, wisdom, charisma)
        else:
            return adv.Adventurer(name, age, strength, dexterity, constitution, intelligence, wisdom, charisma)