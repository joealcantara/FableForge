# IMPORTS
# Imports from Python Standard Libraries
import pygame, random, sys

# Imports from other python scripts
import adventurer as adv
from logger import Logger
from engine import Engine
from settings import Settings

class FableForge():
    """
    Main Game Initialisation
    """
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.log = Logger()
        self.engine = Engine()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("FableForge")

    def run_game(self):
        running = True
        self.log.write_to_log("Log Opened")
        self.log.write_to_log("The dice rolled: " + str(Engine.rollDice(20)))
        while running:
            self._check_events()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.log.close_logger()
                running = False
                sys.exit()

    def _update_screen(self):
        self.screen.fill(self.settings.bg_colour)
        pygame.display.update()

    # log = create_logger()
    # bob = createRandomCharacter('Bob')
    # joe = createRandomCharacter('Joe', 'Warrior')
    # bob.printStats()
    # joe.printStats()
    # close_logger(log)

if __name__ == "__main__":
    ff = FableForge()
    ff.run_game()