import pygame as g # in terminal -> pip install pygame
import math as m
import random as r

#Create color constants


#Game constants

PI = m.pi
SIZE = (1900,1060)
FPS = 60

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

    #screen.fill()

    g.display.flip()
    clock.tick(FPS)