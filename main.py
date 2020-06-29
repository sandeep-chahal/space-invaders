import pygame
import os
import time
import random

import util
from background import Background
from ship import Player

pygame.font.init()

# setup screen
WIDTH, HEIGHT = 800, 600
pygame.display.set_caption("Space Invaders")
screen = pygame.display.set_mode((WIDTH, HEIGHT))


def main():
    game_start = True
    game_over = False
    FPS = 60
    clock = pygame.time.Clock()

    background = Background(screen, WIDTH, HEIGHT)
    background.render()

    player = Player(screen, 300, 300)

    while True:
        clock.tick(FPS)  # set fps

        background.scroll(1)

        player.init_controller()
        player.render()

        pygame.display.update()
        util.check_quit(pygame)  # check for quit event


main()
