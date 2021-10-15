import pygame as g # in terminal -> pip install pygame
import math as m
import random as r

# Create color constants

BLACK = (0, 0, 0)
RED = (255, 0, 21)
WHITE = (255, 255, 255)
BULLET = (135, 89, 3)
DESERT = (214, 163, 66)
HAT = (61, 21, 4)
TUMBLE = (79, 64, 2)

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
    g.draw.ellipse(screen, WHITE, [55, 5, 45, 45])
    g.draw.ellipse(screen, BLACK, [55, 5, 45, 45], width=3)
    g.draw.lines(screen, BLACK, False, ([77.5, 50], [77.5, 105], [55,155], [77.5, 105], [100, 155]), width=3)
    g.draw.line(screen, BLACK, [77.5, 77.5], [50, 72], width=3)

    # GUN
    gun = g.image.load('PngItem_4917920.png').convert_alpha()
    gun = g.transform.scale(gun,[60,30])
    screen.blit(gun, [0,57.5])

    g.draw.line(screen, BLACK, [77.5, 77.5], [50, 83], width=3)

    # HAT
    g.draw.line(screen, HAT, [45, 15],[110, 15],width=5)
    g.draw.circle(screen, HAT, [70, 15], 15, draw_top_right = True, draw_top_left = True)
    g.draw.circle(screen, HAT, [85, 15], 15, draw_top_right=True, draw_top_left=True)

    # Tumbleweed

    g.draw.arc(screen, TUMBLE, [300,300,150,150], 3.14, 0, width=4)
    g.draw.arc(screen, TUMBLE, [300, 350, 150, 150], 2*3.14, 2.5, width=4)
    g.draw.arc(screen, TUMBLE, [350, 275, 150, 150], 5, 2.5, width=4)
    g.draw.arc(screen, TUMBLE, [300, 300, 150, 150], 3.14, 0, width=4)

    g.display.flip()

    clock.tick(FPS)