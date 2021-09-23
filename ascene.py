import pygame as g
import math as m
import random as r

#Create color constants
FRONTGRAY = (102, 106, 112)
BACKGRAY = (71, 73, 77)
SKY = (39, 139, 232)
WINDOW = (213, 223, 224)
WINDOWSHADE = (161, 170, 171)
PAVEMENT = (26, 27, 28)

#Game constants

PI = m.pi
SIZE = (1900,1000)
FPS = 60

#########################################################

g.init()

screen = g.display.set_mode(SIZE)
g.display.set_caption("Jame Scene")
clock = g.time.Clock()

running = True
while running:
    for event in g.event.get():
        if event.type == g.QUIT:
            running = False

    screen.fill(SKY)
    g.draw.rect(screen,BACKGRAY,[600,0,900,950])

    g.display.flip()
    clock.tick(FPS)