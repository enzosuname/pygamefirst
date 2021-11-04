import pygame as g
import math as m
import random as r

# Create color constants

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 21)
BULLET = (135, 89, 3)
DESERT = (214, 163, 66)
HAT = (61, 21, 4)

# Game constants

PI = m.pi
DISPLAY_WIDTH = 1100
DISPLAY_LENGTH = 850
SIZE = (DISPLAY_WIDTH,DISPLAY_LENGTH)
FPS = 60

# def for similar attributes

class enema:
    def __init__(self, display, x, y, width, height):
        self.display = display
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw_man(self):

        # Man
        g.draw.ellipse(screen, WHITE, [55 + self.x, 5 + self.y, 45 + self.width, 45 + self.height])
        g.draw.ellipse(screen, BLACK, [55 + self.x, 5 + self.y, 45 + self.width, 45 + self.height], width=3)
        g.draw.lines(screen, BLACK, False, ([77.5 + self.x, 50 + self.y], [77.5 + self.x, 105 + self.y],\
                                            [55 + self.x, 155 + self.y], [77.5 + self.x, 105 + self.y], \
                                            [100 + self.x, 155 + self.y]), width=3)
        g.draw.line(screen, BLACK, [77.5 + self.x, 77.5 + self.y], [50 + self.x, 72 + self.y], width=3)

        # GUN
        gun = g.image.load('PngItem_4917920.png').convert_alpha()
        gun = g.transform.scale(gun, [60, 30])
        screen.blit(gun, [0 + self.x, 57.5 + self.y])

        g.draw.line(screen, BLACK, [77.5 + self.x, 77.5 + self.y], [50 + self.x, 83 + self.y], width=3)

        # HAT
        g.draw.line(screen, HAT, [45 + self.x, 15 + self.y], [110 + self.x, 15 + self.y], width=5)
        g.draw.circle(screen, HAT, [70 + self.x, 15 + self.y], 15, draw_top_right=True, draw_top_left=True)
        g.draw.circle(screen, HAT, [85 + self.x, 15 + self.y], 15, draw_top_right=True, draw_top_left=True)

    def draw_bullet(self):

        g.draw.ellipse(screen, BULLET, [0 + self.x, 0 + self.y, 45, 15])
        g.draw.rect(screen, BULLET, [22.5 + self.x, 0 + self.y, 23, 15])


#########################################################

g.init()

# game dependents
screen = g.display.set_mode(SIZE)
g.display.set_caption("Jame Scene")
clock = g.time.Clock()

# create enemas
bullet_list = []
for call in range(4):
    bullet_list.append(enema(screen, 0, 0, 0, 0))

enema_list = []
for call in range(4):
    enema_list.append(enema(screen, 950, 690 - (call * 200), 0, 0))




# game
running = True
while running:
    for event in g.event.get():
        if event.type == g.QUIT:
            running = False

    # screen.fill(DESERT)
    desert = g.image.load('western.jpg')
    desert = g.transform.scale(desert, [1100, 850])
    screen.blit(desert, [0, 0])

    for enema in enema_list:
        enema.draw_man()

    for bullet in bullet_list:
        enema.draw_bullet()

    g.display.flip()

    clock.tick(FPS)