import pygame as g # in terminal -> pip install pygame
import math as m
import random as r

# Create color constants

BLACK = (0, 0, 0)
RED = (255, 0, 21)
WHITE = (255, 255, 255)
BULLET = (135, 89, 3)
DESERT = (214, 163, 66)
HAT = (38, 12, 13)

# Game constants

PI = m.pi
DISPLAY_WIDTH = 1900
DISPLAY_LENGTH = 1060
SIZE = (DISPLAY_WIDTH, DISPLAY_LENGTH)
FPS = 60

# Game classes

#class bagoinga():
    #def __init__(self):

    #def move_bagoinga(self):

# def for similar attributes

#########################################################

g.init()

# game dependents
screen = g.display.set_mode(SIZE)
g.display.set_caption("Cowboy, baby")
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

    # Man
    g.draw.ellipse(screen, WHITE, [500, 500, 45, 45])
    g.draw.ellipse(screen, BLACK, [500, 500, 45, 45], width=3)
    g.draw.lines(screen, BLACK, False, ([522.5, 545], [522.5, 600], [500,650], [522.5, 600], [545, 650]), width=3)
    g.draw.line(screen, BLACK, [522.5, 572.5], [495, 567], width=3)

    # GUN
    gun = g.image.load('C:\\Users\\17536\\Desktop\\pygame images\\PngItem_4917920.png').convert_alpha()
    # This image is currently directly mapped through my directory, presumably on github it wouldn't also work?

    gun = g.transform.scale(gun,[60,30])
    screen.blit(gun, [445,555])

    g.draw.line(screen, BLACK, [522.5, 572.5], [495, 578], width=3)

    # HAT
    g.draw.line(screen, HAT, [490, 510],[555, 510],width=5)
    #g.draw.ellipse(screen, HAT, [])
    g.draw.arc(screen, HAT, [522.5, 475, 22.5, 25], 0, 3.14, width = 3)

    g.display.flip()

    clock.tick(FPS)