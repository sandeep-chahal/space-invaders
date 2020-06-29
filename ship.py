import pygame
from os import path
import random
from laser import Laser


def scale_ship(ship):
    return pygame.transform.scale(ship, (50, 50))


def scale_laser(ship):
    return pygame.transform.scale(ship, (5, 40))


# loading ships and laser
player_ship = scale_ship(pygame.image.load(
    path.join("assets", "playerShip2_green.png")))
player_laser = scale_laser(pygame.image.load(
    path.join("assets", "laserGreen07.png")))

enemy_ship_black = scale_ship(pygame.image.load(
    path.join("assets", "enemyBlack2.png")))

enemy_ship_green = scale_ship(pygame.image.load(
    path.join("assets", "enemyGreen3.png")))

enemy_ship_green2 = scale_ship(pygame.image.load(
    path.join("assets", "enemyGreen4.png")))

enemy_ship_red = scale_ship(pygame.image.load(
    path.join("assets", "enemyRed2.png")))

enemy_ship_red2 = scale_ship(pygame.image.load(
    path.join("assets", "enemyRed4.png")))

enemy_laser_red = scale_laser(pygame.image.load(
    path.join("assets", "laserRed01.png")))

enemy_laser_green = scale_laser(pygame.image.load(
    path.join("assets", "laserGreen11.png")))

enemy_ships = [(enemy_ship_black, enemy_laser_red), (enemy_ship_red, enemy_laser_red),
               (enemy_ship_red2, enemy_laser_red), (enemy_ship_green, enemy_laser_green), (enemy_ship_green2, enemy_laser_green)]


class Ship():
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.ship_img = None
        self.laser_img = None
        self.ship_speed = None
        self.lasers = []
        self.shoot_cooldown = 0

    def render(self):
        self.screen.blit(self.ship_img, (self.x, self.y))

    def operate_lasers(self):
        if(self.shoot_cooldown > 0):
            self.shoot_cooldown -= 1
        for laser in self.lasers:
            laser.move()
            if laser.offscreen():
                self.lasers.remove(laser)
            else:
                laser.render()

    def shoot(self, x, y):
        if self.shoot_cooldown == 0:
            self.shoot_cooldown = 45
            laser = Laser(self.screen, self.laser_img, x, y, self.laser_speed)
            self.lasers.append(laser)

    def get_width(self):
        return self.ship_img.get_width()

    def get_height(self):
        return self.ship_img.get_height()


class Player(Ship):
    def __init__(self, screen, x, y, laser_speed):
        super().__init__(screen, x, y)
        self.health = 100
        self.ship_img = player_ship
        self.laser_img = player_laser
        self.ship_speed = 3
        self.laser_speed = laser_speed
        self.shoot_cooldown = 45

    def shoot(self):
        x = self.x+self.ship_img.get_width()/2-2
        y = self.y - self.ship_img.get_height()/2
        super().shoot(x, y)

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
        if keys[pygame.K_SPACE]:
            self.shoot()


class Enemy(Ship):
    def __init__(self, screen, ship, laser, x, y, laser_speed):
        super().__init__(screen, x, y)
        self.x = x
        self.y = y
        self.ship_img = ship
        self.laser_img = laser
        self.ship_speed = 1
        self.laser_speed = laser_speed
        self.rendering = False

    def render(self):
        # only render if ship visible
        if not self.y + self.ship_img.get_height() < 0:
            super().render()
            self.rendering = True

    def in_base(self):
        return self.y > self.screen.get_height()

    def move(self):
        self.y += self.ship_speed

    def shoot(self):
        if random.randrange(0, 120) == 15:
            super().shoot(self.x+self.ship_img.get_width() /
                          2, self.y+self.ship_img.get_height()/2)
