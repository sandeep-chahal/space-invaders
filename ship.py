class Ship():
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.ship_img = None
        self.laser_img = None
        self.lasers = []
        self.laser_speed

    def render(self):
        self.screen.blit(self.ship_img, self.x, self.y)

    def move(self, dir):
        if dir == "UP":
            self.y -= self.ship_speed
        elif dir == "DOWN":
            self.y += self.ship_speed
        elif dir == "RIGHT":
            self.x += self.ship_speed
        elif dir == "LEFT":
            self.x -= self.ship_speed

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
