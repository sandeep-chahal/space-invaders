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


# sound setup
pygame.mixer.init(10100, -16, 2, 64)
pygame.mixer.init()
explosion_sound = pygame.mixer.Sound(
    os.path.join("assets", "explosion_sound.wav"))
explosion_sound.set_volume(0.7)

pygame.mixer.music.load(os.path.join("assets", "bg_music.wav"))
bg_music = pygame.mixer.music
bg_music.play(-1)
bg_music.set_volume(0.5)


def press_enter():
    if pygame.key.get_pressed()[pygame.K_RETURN]:
        return True


def main():
    game_start = False
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

        if not game_start:
            gui.main_menu(screen)
            bg_music.set_volume(1)
            if press_enter():
                game_start = True
        elif game_over:
            gui.show_game_over(screen)
            bg_music.set_volume(0)
            if press_enter():
                level = 0
                player.health = 100
                player.x = 350
                player.y = 400
                player.lasers = []
                enemies = []
                game_over = False
        else:
            background.scroll(0.5)
            bg_music.set_volume(0.6)

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
                            explosion_sound.play()
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
            if player.gameover():
                game_over = True

            gui.show_level(screen, level)

        pygame.display.update()
        util.check_quit(pygame)  # check for quit event


main()
