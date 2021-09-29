import pygame as g # in terminal -> pip install pygame
import math as m
import random as r

#Create color constants

RED = (255, 0, 21)
WHITE = (255, 255, 255)

#Game constants

PI = m.pi
DISPLAY_WIDTH = 1900
DISPLAY_LENGTH = 1060
SIZE = (DISPLAY_WIDTH,DISPLAY_LENGTH)
FPS = 60
rect_x = 950
x_velocity = 5
rect_y = 530
y_velocity = 5
rect_side = 50

#def for similar attributes


#########################################################

g.init()

#game dependents
screen = g.display.set_mode(SIZE)
g.display.set_caption("Jame Scene")
clock = g.time.Clock()
#game
running = True
while running:
    for event in g.event.get():
        if event.type == g.QUIT:
            running = False

    screen.fill(WHITE)

    if rect_x + rect_side >= DISPLAY_WIDTH or rect_x < 0:
        x_velocity *= -1
    if rect_y + rect_side >= DISPLAY_LENGTH or rect_y < 0:
        y_velocity *= -1

    g.draw.rect(screen, RED, [rect_x, rect_y, rect_side, rect_side])
    rect_x += x_velocity
    rect_y += y_velocity

    g.display.flip()

    clock.tick(FPS)