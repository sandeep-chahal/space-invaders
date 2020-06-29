from ship import enemy_ships, Enemy
import random


def check_quit(pygame):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()


def genrate_enemies(screen, level):
    enemies = []
    for i in range(5*level):
        (ship, laser) = random.choice(enemy_ships)
        x, y = gen_pos(enemies, 100, screen.get_width()-100, -1000*level, -100)
        enemy = Enemy(screen, ship, laser, x, y, 4)
        enemies.append(enemy)
    return enemies


# b -> bundries, in which enemy ship will spawn
def gen_pos(enemies, bx1, bx2, by1, by2):
    y = random.randrange(by1, by2)
    x = random.randrange(bx1, bx2)
    for enemy in enemies:
        # check if x,y dont overlap other ships position
        if (enemy.y+enemy.get_height() > y and enemy.y-enemy.get_height() < y) and (enemy.x+enemy.get_width() < x and enemy.x-enemy.get_width() > x):
            return gen_pos(enemies, bx1, bx2, by1, by2)
        else:
            return (x, y)
    return (x, y)
