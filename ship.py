import pygame
from os import path

player_ship = pygame.image.load(path.join("assets", "playerShip2_green.png"))


class Ship():
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.ship_img = None
        self.laser_img = None
        self.ship_speed = None
        self.lasers = []
        self.laser_speed = 5

    def render(self):
        self.screen.blit(self.ship_img, (self.x, self.y))

    def operate_lasers(self, speed):
        for laser in self.lasers:
            laser.move(self.laser_speed)
            if laser.offscreen():
                self.lasers.remove(laser)
            else:
                laser.render()

    def shoot(self):
        pass

    def get_width(self):
        return self.ship_img.get_width()

    def get_height(self):
        return self.ship_img.get_height()


class Player(Ship):
    def __init__(self, screen, x, y):
        super().__init__(screen, x, y)
        self.health = 100
        self.ship_img = player_ship
        self.ship_speed = 3

    def init_controller(self):
        # checking for key presses
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and not self.y - self.ship_speed <= 0:
            self.y -= self.ship_speed
        if keys[pygame.K_DOWN] and not self.y + self.ship_speed + self.ship_img.get_height() >= self.screen.get_height():
            self.y += self.ship_speed
        if keys[pygame.K_RIGHT] and not self.x + self.ship_speed + self.ship_img.get_width() >= self.screen.get_width():
            self.x += self.ship_speed
        if keys[pygame.K_LEFT] and not self.x - self.ship_speed <= 0:
            self.x -= self.ship_speed
