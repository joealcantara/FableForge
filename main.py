import random

def diceRoll(sides):
    return random.randint(1, sides)

def main():
    print("Hello from fableforge!")
    print(diceRoll(20))


if __name__ == "__main__":
    main()
