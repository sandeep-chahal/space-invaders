import pygame
from os import path
pygame.font.init()

classic_font_25 = pygame.font.Font(
    path.join("assets", "ARCADECLASSIC.TTF"), 25)
classic_font_50 = pygame.font.Font(
    path.join("assets", "ARCADECLASSIC.TTF"), 50)


game_over_title = classic_font_50.render("GAME OVER!", 1, (255, 255, 255))
go_width, go_height = classic_font_50.size("GAME OVER!")

play_again_title = classic_font_25.render(
    "press ENTER to play again", 1, (255, 255, 255))
play_again_title_width = classic_font_25.size("press ENTER to play again")[0]


game_start_title = classic_font_50.render("SPACE INVADERS", 1, (255, 255, 255))
gs_width, gs_height = classic_font_50.size("SPACE INVADERS")

play_title = classic_font_25.render(
    "press ENTER to play", 1, (255, 255, 255))
play_title_width = classic_font_25.size("press ENTER to play")[0]


def show_level(screen, level):
    width = classic_font_25.size(f"Level {level}")[0]
    level_title = classic_font_25.render(f"Level {level}", 1, (255, 255, 255))
    screen.blit(level_title, (screen.get_width() - width-10, 10))


def show_game_over(screen):
    screen.blit(game_over_title, (screen.get_width()/2 -
                                  go_width/2, screen.get_height()/2-go_height/2))
    screen.blit(play_again_title, (screen.get_width()/2 -
                                   play_again_title_width/2, screen.get_height()/2+20))


def main_menu(screen):
    screen.blit(game_start_title, (screen.get_width()/2 -
                                   gs_width/2, screen.get_height()/2-gs_height/2))
    screen.blit(play_title, (screen.get_width()/2 -
                             play_title_width/2, screen.get_height()/2+20))
