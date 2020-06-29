import pygame
import os
import time
import random

import util
from background import Background

pygame.font.init()

# setup screen
WIDTH, HEIGHT = 800, 600
pygame.display.set_caption("Space Invaders")
screen = pygame.display.set_mode((WIDTH, HEIGHT))


def main():
    FPS = 60
    clock = pygame.time.Clock()

    background = Background(screen, WIDTH, HEIGHT)
    background.render()

    while True:
        clock.tick(FPS)  # set fps

        background.scroll(1)

        pygame.display.update()
        util.check_quit(pygame)  # check for quit event


main()
