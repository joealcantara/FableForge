# IMPORTS
# Imports from Python Standard Libraries
import pygame, random, sys

# Imports from other python scripts
import adventurer as adv
import engine as eng
from settings import Settings

class FableForge():
    """
    Main Game Initialisation
    """
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("FableForge")


    def run_game(self):
        running = True
        while running:
            self._check_events()
            self._update_screen()
            self.clock.tick(60)



    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print('Game Ended')
                running = False
                pygame.quit()
                sys.exit()


    def _update_screen(self):
        self.screen.fill(self.settings.bg_colour)
        pygame.display.update()


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

def create_logger():
    file = open("log.txt", "w+")
    file.write("Log open\n")
    return file

def close_logger(log):
    log.write("Log closed")
    log.close()





    log = create_logger()
    bob = createRandomCharacter('Bob')
    joe = createRandomCharacter('Joe', 'Warrior')
    bob.printStats()
    joe.printStats()
    close_logger(log)

if __name__ == "__main__":
    ff = FableForge()
    ff.run_game()