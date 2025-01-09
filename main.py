# This is the main part of the program.
import adventurer as adv
import random


def rollDice(sides):
    return random.randrange(1, sides)

def createRandomCharacter(name, charClass = None):
    strength = rollDice(20)
    dexterity = rollDice(20)
    constitution = rollDice(20)
    intelligence = rollDice(20)
    wisdom = rollDice(20)
    charisma = rollDice(20)
    age = rollDice(100)
    if charClass == 'Warrior':
        return adv.Warrior(name, age, strength, dexterity, constitution, intelligence, wisdom, charisma)
    else:
        return adv.Adventurer(name, age, strength, dexterity, constitution, intelligence, wisdom, charisma)

def main():
    bob = createRandomCharacter('Bob')
    joe = createRandomCharacter('Joe', 'Warrior')
    bob.printStats()
    joe.printStats()

if __name__ == "__main__":
    main()