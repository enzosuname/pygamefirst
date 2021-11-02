import pygame as g # in terminal -> pip install pygame
import math as m
import random as r

# Create color constants

BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
GRAY = (92, 94, 92)
DRKGRAY = (69, 66, 66)

# Game constants

PI = m.pi
DISPLAY_WIDTH = 1900
DISPLAY_LENGTH = 1060
SIZE = (DISPLAY_WIDTH,DISPLAY_LENGTH)
FPS = 60
g.font.init()
font = g.font.SysFont('Ariel', 25, True, False)

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
        self.counter = 0

    def draw_ship(self):
        g.draw.ellipse(self.display, self.color, (self.x, self.y, self.width, self.height))
        g.draw.rect(self.display, GRAY, (self.x+5, self.y+20, self.width-10, self.height-40))

    def draw_box(self):
        g.draw.ellipse(self.display, self.color, [self.x, self.y, self.width, self.height])
        g.draw.rect(screen, BLACK, [self.x, self.y, self.width, self.height-22])

        #g.draw.rect(self.display, self.color, (self.x, self.y, self.width, self.height))

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
        g.draw.rect(self.display, RED, [0, 0, 1900 - self.counter * 4, 100])
        text = font.render(f"Wow! {self.counter}", True, BLACK)
        screen.blit(text, [250, 250])
        if (self.x <= other.x <= self.x+self.width or self.x <= other.x+other.width\
                <= self.x+self.width) and (self.y < other.y < self.y+self.height or \
                self.y < other.y+other.height < self.y+self.height):

            self.counter += 1

            # Explosion animation every time ship is hit
            explosion = g.image.load('explosion.png').convert_alpha()
            explosion = g.transform.scale(explosion, [160, 160])
            screen.blit(explosion, [self.x-85, self.y-40])

        if self.counter == 475:
            gameover = font.render(f"GAME OVER", True, RED)
            screen.blit(gameover, [950, 530])
#########################################################

g.init()

# game dependents
screen = g.display.set_mode(SIZE)
g.display.set_caption("Dodge the missiles!")
clock = g.time.Clock()

# create player
player_width = 25
player_height = 100
x_loc = (DISPLAY_WIDTH-player_width)/2
y_loc = DISPLAY_LENGTH - 2*player_width
player = Box(screen, x_loc, y_loc, player_width, player_height, DRKGRAY)

# create enemies
enemy_width = 15
enemy_height = 45
enemy_list=[]
for i in range(10):
    x_coord = r.randrange(0, DISPLAY_WIDTH, 5)
    random_y = r.randrange(-100, 0, 5)
    enemy_list.append(Box(screen, x_coord, random_y, enemy_width, enemy_height, BLACK))

g.mouse.set_visible(True)

# game
running = True
while running:

    pos = g.mouse.get_pos()
    player.x = pos[0]-.5*player_width
    player.y = pos[1]-.5*player_height

    for event in g.event.get():
        if event.type == g.QUIT:
            running = False


    screen.fill(BLUE)

    player.draw_ship()

    for enemy in enemy_list:
        enemy.draw_box()
        enemy.drop_box()
        if player.is_collided(enemy):
            running = False

    player.update()

    yeet = 'woah'


    g.display.flip()
    clock.tick(FPS)