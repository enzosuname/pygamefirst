import pygame as g # in terminal -> pip install pygame
import math as m
import random as r

# Create color constants

RED = (255, 0, 0)
WHITE = (255, 255, 255)

# Game constants

PI = m.pi
DISPLAY_WIDTH = 1900
DISPLAY_LENGTH = 1060
SIZE = (DISPLAY_WIDTH,DISPLAY_LENGTH)
FPS = 60

# def for similar attributes

class Box():
    def __init__(self, display, x, y, width, height):
        self.display = display
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed_x = 0
        self.speed_y = 0

    def draw_box(self):
        g.draw.rect(self.display, RED, (self.x, self.y, self.width, self.height))

    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y

        if self.x <=0:
            self.x = 0
        elif self.x + self.width >= DISPLAY_WIDTH:
            self.x = DISPLAY_WIDTH - self.width

#########################################################

g.init()

# game dependents
screen = g.display.set_mode(SIZE)
g.display.set_caption("Jame Scene")
clock = g.time.Clock()

# create player
player_width = 50
x_loc = (DISPLAY_WIDTH-player_width)/2
y_loc = DISPLAY_LENGTH - 2*player_width
player = Box(screen, x_loc, y_loc, player_width, player_width)

# create enemies
enemy_width = 50
enemy_list=[]
for i in range(7):
    x_coord = i * enemy_width // 6
    random_y = r.randrange(-100, 0, 5)
    enemy_list.append(Box(screen, x_coord, random_y, enemy_width, enemy_width))

# game
running = True
while running:
    for event in g.event.get():
        if event.type == g.QUIT:
            running = False
        if event.type == g.KEYDOWN:
            if event.key == g.K_RIGHT:
                player.speed_x = 5
            if event.key == g.K_LEFT:
                player.speed_x = -5
            if event.key == g.K_UP:
                player.speed_y = -5
            if event.key == g.K_DOWN:
                player.speed_y = 5
        if event.type == g.KEYUP:
            if event.key == g.K_RIGHT:
                player.speed_x = 0
            if event.key == g.K_LEFT:
                player.speed_x = 0
            if event.key == g.K_UP:
                player.speed_y = 0
            if event.key == g.K_DOWN:
                player.speed_y = 0

    screen.fill(WHITE)
    player.draw_box()
    player.update()

    for enemy in enemy_list:
        enemy.draw_box()
        enemy.drop_box()

        if enemy.y > DISPLAY_LENGTH:
            enemy.y = r.randrange(-100, 0, 5)

    g.display.flip()
    clock.tick(FPS)