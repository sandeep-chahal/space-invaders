import pygame
import os


class Background():
    def __init__(self, screen, width, height):
        self.screen = screen
        self.HEIGHT = height
        self.WIDTH = width
        self.BG1 = {"y": 0, "img": pygame.transform.scale(
            pygame.image.load(os.path.join("assets", "bg.jpg")), (self.WIDTH, self.HEIGHT))}
        self.BG2 = {"y": -self.HEIGHT, "img": pygame.transform.scale(
            pygame.image.load(os.path.join("assets", "bg.jpg")), (self.WIDTH, self.HEIGHT))}

    def render(self):
        self.screen.blit(self.BG1['img'], (0, self.BG1["y"]))
        self.screen.blit(self.BG2['img'], (0, self.BG2["y"]))

    def scroll(self, level):
        # check if bg image off screen, if it is reset posiiton
        if self.BG1["y"] > self.HEIGHT:
            self.BG1["y"] = -self.HEIGHT

        if self.BG2["y"] > self.HEIGHT:
            self.BG2["y"] = -self.HEIGHT

        # move bg downward
        self.BG1["y"] += level
        self.BG2["y"] += level
        self.render()
