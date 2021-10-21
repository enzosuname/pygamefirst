import pygame as g # in terminal -> pip install pygame
import math as m
import random as r

# Create color constants

RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

# Game constants

PI = m.pi
DISPLAY_WIDTH = 1900
DISPLAY_LENGTH = 1060
SIZE = (DISPLAY_WIDTH,DISPLAY_LENGTH)
FPS = 60

# def for similar attributes

class Box():
    def __init__(self, display, x, y, width, height, color):
        self.display = display
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.speed_x = 0
        self.speed_y = r.randint(3, 5)

    def draw_box(self):
        g.draw.rect(self.display, self.color, (self.x, self.y, self.width, self.height))

    def drop_box(self):
        if self.y > DISPLAY_LENGTH:
            self.x = r.randrange(0, DISPLAY_WIDTH, 5)
            self.y = r.randrange(-100, 0, 5)

        self.y += self.speed_y

    def update(self):
        self.x += self.speed_x

        if self.x <=0:
            self.x = 0
        elif self.x + self.width >= DISPLAY_WIDTH:
            self.x = DISPLAY_WIDTH - self.width

    def is_collided(self, other):
        counter = 0
        if (self.x <= other.x <= self.x+self.width or self.x <= other.x+other.width\
                <= self.x+self.width) and (self.y < other.y < self.y+self.width or \
                self.y < other.y+other.width < self.y+self.width):

            counter += 1
            self.color = RED

        # test_list = [(self.x, self.y),(self.x+self.width, self.y),(self.x, self.y+self.width),\
        #              (self.x+self.width, self.y+self.width)]
        # other_list = [(other.x, other.y),(other.x+other.width, other.y),(other.x, other.y+other.width),\
        #              (other.x+other.width, other.y+other.width)]
        #
        # for coord in test_list
        #     if coord >= (other.x, other.y) and coord
        #
        # self.x --> other.x
        # self.y --> other.y
        # self.width --> other.width

#########################################################

g.init()

# game dependents
screen = g.display.set_mode(SIZE)
g.display.set_caption("Jame Scene")
clock = g.time.Clock()

# create player
player_width = 50
x_loc = (DISPLAY_WIDTH-player_width)/2
y_loc = DISPLAY_LENGTH - 2*player_width
player = Box(screen, x_loc, y_loc, player_width, player_width, BLUE)

# create enemies
enemy_width = 20
enemy_list=[]
for i in range(10):
    x_coord = r.randrange(0, DISPLAY_WIDTH, 5)
    random_y = r.randrange(-100, 0, 5)
    enemy_list.append(Box(screen, x_coord, random_y, enemy_width, enemy_width, RED))

g.mouse.set_visible(False)

# game
running = True
while running:

    pos = g.mouse.get_pos()
    player.x = pos[0]-.5*player_width
    player.y = pos[1]-.5*player_width

    #pressed_lft = g.mouse.get_pressed()[0]
    for event in g.event.get():
        if event.type == g.QUIT:
            running = False
        # if event.type == g.KEYDOWN:
        #     if event.key == g.K_RIGHT:
        #         player.speed_x = 5
        #     if event.key == g.K_LEFT:
        #         player.speed_x = -5
        # if event.type == g.KEYUP:
        #     if event.key == g.K_RIGHT:
        #         player.speed_x = 0
        #     if event.key == g.K_LEFT:
        #         player.speed_x = 0

    screen.fill(WHITE)

    for enemy in enemy_list:
        enemy.draw_box()
        enemy.drop_box()
        if player.is_collided(enemy):
            running = False

    player.draw_box()
    player.update()

    g.display.flip()
    clock.tick(FPS)