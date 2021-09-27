import pygame as g
import math as m
import random as r

#Create color constants
FRONTGRAY = (102, 106, 112)
BACKGRAY = (71, 73, 77)
SKY = (39, 139, 232)
WINDOW = (213, 223, 224)
BLACKSHADE = (15, 1, 3)
PAVEMENT = (26, 27, 28)
DOOR = (130, 5, 23)

#Game constants

PI = m.pi
SIZE = (1900,1000)
FPS = 60

#def for similar attributes

def building(color,xmod=0):
    #Structure Draw
    g.draw.rect(screen, color, [600+xmod,75,300,925])

    #Door
    g.draw.rect(screen, DOOR, [675+xmod,900,150,100])
    g.draw.line(screen, BLACKSHADE,[750.5+xmod,900],[750.5+xmod,1000],width=2)
    g.draw.circle(screen,BLACKSHADE,[735+xmod,950],3)
    g.draw.circle(screen, BLACKSHADE, [765 + xmod, 950], 3)

    #Windows
    for number in range(8):
        g.draw.rect(screen, WINDOW, [650 + xmod, 125 + (100 * number), 50, 50])
        g.draw.rect(screen, WINDOW, [800 + xmod, 125 + (100 * number), 50, 50])
        g.draw.line(screen, BLACKSHADE, [675.5 + xmod, 125 + (100 * number)], [675.5 + xmod, 175 + (100 * number)],
                    width=2)
        g.draw.line(screen, BLACKSHADE, [825.5 + xmod, 125 + (100 * number)], [825.5 + xmod, 175 + (100 * number)],
                    width=2)
        g.draw.line(screen, BLACKSHADE, [650 + xmod, 150.5 + (100 * number)], [700 + xmod, 150.5 + (100 * number)],
                    width=2)
        g.draw.line(screen, BLACKSHADE, [800 + xmod, 150.5 + (100 * number)], [850 + xmod, 150.5 + (100 * number)],
                    width=2)

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

    #call for building function to form the skyscrapers
    building(BACKGRAY)
    building(BACKGRAY, 400)
    building(FRONTGRAY,-400)
    building(FRONTGRAY, 800)

    g.display.flip()
    clock.tick(FPS)