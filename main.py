import pygame
import os
import time
import random

import util
from background import Background
from ship import Player
import gui


# setup screen
WIDTH, HEIGHT = 800, 600
pygame.display.set_caption("Space Invaders")
screen = pygame.display.set_mode((WIDTH, HEIGHT))


def main():
    game_start = True
    game_over = False
    FPS = 60
    level = 0
    enemies = []
    clock = pygame.time.Clock()

    background = Background(screen, WIDTH, HEIGHT)
    background.render()

    player = Player(screen, 350, 400, -5)

    while True:
        clock.tick(FPS)  # set fps
        background.scroll(1)
        # gui.show_level(screen, level)
        gui.show_level(screen, player.health)

        # if no enemy left, level up and generate more
        if(len(enemies) == 0):
            level += 1
            enemies = util.genrate_enemies(screen, level)

        for enemy in enemies:
            enemy.move()
            #  if rendering and in base
            if enemy.rendering:
                enemy.shoot()
                enemy.operate_lasers()
                if enemy.in_base():
                    player.health -= 10
                    enemies.remove(enemy)
            enemy.render()

        player.init_controller()
        player.operate_lasers()
        player.render()

        pygame.display.update()
        util.check_quit(pygame)  # check for quit event


main()
