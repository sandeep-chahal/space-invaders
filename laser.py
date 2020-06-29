class Laser():
    def __init__(self, screen, laser_img, x, y, speed):
        self.laser_img = laser_img
        self.speed = speed
        self.screen = screen
        self.y = y
        self.x = x

    def move(self):
        self.y += self.speed

    def render(self):
        self.screen.blit(self.laser_img, (self.x, self.y))

    def offscreen(self):
        return self.y + self.laser_img.get_height() < 0 or self.y > self.screen.get_height()
