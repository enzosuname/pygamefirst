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
SUN = (227, 209, 11)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

#Game constants

PI = m.pi
SIZE = (1900,1060)
FPS = 60

#def for similar attributes

def building(color,xmod=0):
    #Structure Draw
    g.draw.rect(screen, color, [600+xmod,75,300,925],border_top_right_radius=5,border_top_left_radius=5)

    #Door
    g.draw.rect(screen, DOOR, [675+xmod,900,150,100])
    g.draw.line(screen, BLACKSHADE,[750.5+xmod,900],[750.5+xmod,1000],width=2)
    g.draw.circle(screen,BLACKSHADE,[735+xmod,950],3)
    g.draw.circle(screen, BLACKSHADE, [765 + xmod, 950], 3)

    #Windows
    for number in range(8):
        g.draw.rect(screen, WINDOW, [650 + xmod, 125 + (100 * number), 50, 50],border_radius=3)
        g.draw.rect(screen, WINDOW, [800 + xmod, 125 + (100 * number), 50, 50],border_radius=3)
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

    #sky and sun
    screen.fill(SKY)
    g.draw.circle(screen, SUN, [0, 0], 200)

    #call for building function to form the skyscrapers
    building(BACKGRAY)
    building(BACKGRAY, 400)
    building(FRONTGRAY,-400)
    building(FRONTGRAY, 800)

    #pavement
    g.draw.rect(screen, PAVEMENT, [0 , 1000, 1920, 60])


    #animation P.S ANIMATION IS REALLY INEFFICIENT, UNLIKE REST OF DRAWING, JUST WANTED TO MOVE ON.

    for event in g.event.get():
        if event.type == g.MOUSEBUTTONDOWN:
            g.draw.rect(screen, SKY, [675,900,150,100])
            g.draw.rect(screen, FRONTGRAY, [685, 920, 25,80])
            g.draw.rect(screen, BACKGRAY, [720, 920, 25,80])
            g.draw.rect(screen, BACKGRAY, [755, 920, 25, 80])
            g.draw.rect(screen, FRONTGRAY, [790, 920, 25, 80])
            for number in range(8):
                g.draw.rect(screen, WINDOW, [689, 924 + (8 * number), (25 / 300) * 50, (25 / 300) * 50],
                            border_radius=1)
                g.draw.rect(screen, WINDOW, [702, 924 + (8 * number), (25 / 300) * 50, (25 / 300) * 50],
                            border_radius=1)
                g.draw.rect(screen, WINDOW, [724, 924 + (8 * number), (25 / 300) * 50, (25 / 300) * 50],
                            border_radius=1)
                g.draw.rect(screen, WINDOW, [737, 924 + (8 * number), (25 / 300) * 50, (25 / 300) * 50],
                            border_radius=1)
                g.draw.rect(screen, WINDOW, [759, 924 + (8 * number), (25 / 300) * 50, (25 / 300) * 50],
                            border_radius=1)
                g.draw.rect(screen, WINDOW, [772, 924 + (8 * number), (25 / 300) * 50, (25 / 300) * 50],
                            border_radius=1)
                g.draw.rect(screen, WINDOW, [794, 924 + (8 * number), (25 / 300) * 50, (25 / 300) * 50],
                            border_radius=1)
                g.draw.rect(screen, WINDOW, [807, 924 + (8 * number), (25 / 300) * 50, (25 / 300) * 50],
                            border_radius=1)
            g.draw.rect(screen, DOOR, [691.25, 987.5, 12.5, 8.5])
            g.draw.rect(screen, DOOR, [726.25, 987.5, 12.5, 8.5])
            g.draw.rect(screen, DOOR, [761.25, 987.5, 12.5, 8.5])
            g.draw.rect(screen, DOOR, [796.25, 987.5, 12.5, 8.5])
            g.draw.rect(screen, PAVEMENT, [675, 995, 150, 5])
            g.draw.line(screen, DOOR, [675,900], [675,1000], width=4)
            g.draw.line(screen, DOOR, [825,900], [825, 1000], width=4)

            #range acts as a shawty fix to keep animation going given it's a fixed image, breaks stop program however.
            #i would imagine there's a better solution

            for num in range(999):
                g.display.flip()
            #    g.draw

    g.display.flip()
    clock.tick(FPS)