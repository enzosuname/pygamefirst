import pygame as g
import math as m
import random as r

#Create color constants
WHITE = (255,255,255)
RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
BLACK = (0,0,0)
COLORS = [WHITE, BLUE, GREEN, BLACK]

#Math constant

PI = m.pi

#Game constants

SIZE = (1900,1000)
FPS = 60

#####################

g.init()

screen = g.display.set_mode(SIZE)
g.display.set_caption("My First Pygame")
clock = g.time.Clock()

running = True
while running:
    #get all keyboard, mouse, etc, events
    for event in g.event.get():
        if event.type == g.QUIT:
            running = False
        elif event.type == g.KEYDOWN:
            print("You pressed a key down!")
        elif event.type == g.KEYUP:
            print("You pressed a key up!")
        elif event.type == g.MOUSEBUTTONDOWN:
            print("You clicker you!")

    # game logic

    screen.fill(RED)

    g.draw.rect(screen,BLUE,[0,60,700,375],5,border_radius=10)
    g.draw.arc(screen,GREEN,[55,50,200,200],0, 5*PI/4, width=5)

    for multiplier in range(10):
        color = r.choice(COLORS)
        g.draw.line(screen,color,(10 +5*multiplier, 10),(500,200),5)

    g.display.flip()



    clock.tick(FPS)

g.quit()