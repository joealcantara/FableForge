# This is the main part of the program.
import adventurer as adv

def main():
    bob = adv.Adventurer("bob", 42)
    print(bob.name)
    print(bob.age)
    

if __name__ == "__main__":
    main()