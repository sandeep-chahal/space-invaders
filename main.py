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
        gui.show_level(screen, level)

        # if no enemy left, level up and generate more
        if(len(enemies) == 0):
            level += 1
            enemies = util.genrate_enemies(screen, level)

        # ----------------------------- enemies -----------------------------
        for enemy in enemies:
            enemy.move()  # move downward
            #  if enemy is rendering(if enemy is on screen)
            if enemy.rendering:
                enemy.shoot()  # shoot lasers
                enemy.operate_lasers()  # move lasers
                # if enemy ship enters base (if it pass by player and goes down the screen)
                if enemy.in_base():
                    player.health -= 20
                    enemies.remove(enemy)
                # check if player laser hits enemy ship
                for laser in player.lasers:
                    if util.collide(enemy, laser):
                        player.lasers.remove(laser)
                        enemies.remove(enemy)
                # check if enemy laser collides with player
                for laser in enemy.lasers:
                    if util.collide(player, laser):
                        enemy.lasers.remove(laser)
                        player.health -= 10
            enemy.render()

        # -----------------------------player-----------------------------
        player.init_controller()
        player.operate_lasers()
        player.render()

        pygame.display.update()
        util.check_quit(pygame)  # check for quit event


main()
