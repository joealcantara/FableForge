# Import python standard libraries
import random

# Import user made libraries
import characters as ch, quests as qu

def resolveQuest(power, difficulty):
    roll = diceRoll(20)
    print("You rolled, ", roll)
    if roll + power < difficulty:
        return 'Failed'
    else:
        return 'Success'

def diceRoll(sides):
    return random.randint(1, sides)

def main():
    print("Hello from fableforge!")
    print(diceRoll(20))
    c1 = ch.Character("John", 12)
    print(c1.name)
    print(c1.power)
    q1 = qu.Quest("First Quest", 20)
    print(q1.title)
    print(q1.difficulty)
    print(resolveQuest(c1.power, q1.difficulty))



if __name__ == "__main__":
    main()
