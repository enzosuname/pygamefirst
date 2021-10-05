import pygame as g # in terminal -> pip install pygame
import math as m
import random as r

# Create color constants

RED = (255, 0, 21)
WHITE = (255, 255, 255)
BULLET = (135, 89, 3)
DESERT = (214, 163, 66)

# Game constants

PI = m.pi
DISPLAY_WIDTH = 1900
DISPLAY_LENGTH = 1060
SIZE = (DISPLAY_WIDTH, DISPLAY_LENGTH)
FPS = 60
rect_x = 950
x_velocity = 5
rect_y = 530
y_velocity = 5
rect_side = 50

# Game classes

#class bagoinga():
    #def __init__(self):

    #def move_bagoinga(self):

# def for similar attributes

#########################################################

g.init()

# game dependents
screen = g.display.set_mode(SIZE)
g.display.set_caption("Jame Scene")
clock = g.time.Clock()
# game
running = True
while running:
    for event in g.event.get():
        if event.type == g.QUIT:
            running = False

    screen.fill(DESERT)

    # Initial framing of bullet, will come back to animate once the parts have formed
    g.draw.ellipse(screen, BULLET, [0, 0, 45, 15])
    g.draw.rect(screen, BULLET, [22.5, 0, 23, 15])



    g.display.flip()

    clock.tick(FPS)