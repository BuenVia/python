import sys

import pygame

class Rocket:

    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption('Rocket Game')

    def run_game(self):
        while True:
            for event in pygame.event.get():
                self._check_events()

    def _check_events(self):
        # QUIT
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            self._check_keydown_events(event)
        
        elif even.type == pygame.KEYUP:
            self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.rocket

    def _check_keyup_events(self, event):