import pygame as g
import math as m
import random as r

# User controls the cowboy using up and down arrow keys
# Avoid getting hit by the bullets three times
# When guns fire bullets, a gunshot noise should be heard
# Also Western music should be heard in the background

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
g.font.init()
font = g.font.SysFont('Ariel', 80, True, False)

# def for similar attributes
class bullet:
    def __init__(self, display, x, y, width=45.5, height=15):
        self.display = display
        self.x = x
        self.y = y
        self.x_velo = r.randint(5, 50)
        self.width = width
        self.height = height

        # self.last = g.time.get_ticks()
        # self.cooldown = 500

    def shoot_bullet(self):
        if self.x < 0:
            self.x = 885
            GUNSOUND.play()
        self.x -= self.x_velo

    def draw_bullet(self):
        g.draw.ellipse(screen, BULLET, [0 + self.x, 0 + self.y, 45, 15])
        g.draw.rect(screen, BULLET, [22.5 + self.x, 0 + self.y, 23, 15])

        # now = g.time.get_ticks()
        # if now - self.last >= self.cooldown:
        #     self.last = now
        #     g.draw.ellipse(screen, BULLET, [500,500,500,500])

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

class man:
    def __init__(self, display, x, y, width=70, height=170):
        self.display = display
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.cowboy = g.image.load('cowboy.png').convert_alpha()
        self.counter = 3
        self.heart = g.image.load('heart.png').convert_alpha()
        self.dead = False
        self.last = g.time.get_ticks()
        self.cooldown = 3000

    def draw_good_man(self):
        self.cowboy = g.transform.scale(self.cowboy, [self.width, self.height])
        self.display.blit(self.cowboy, [100 + self.x, 100 + self.y])

    def is_collided(self, other):
        if (self.x <= other.x <= self.x+self.width or self.x <= other.x+other.width\
                <= self.x+self.width) and (self.y < other.y < self.y+self.height or \
                self.y < other.y+other.height < self.y+self.height):

            self.counter -= 1
            other.x = 885
            GUNSOUND.play()

        # I COULDN'T GET A FOR LOOP TO WORK SO I WENT LAZY OPTION SORRY

        if self.counter == 3:
            self.display.blit(self.heart,[0,0])
            self.display.blit(self.heart, [48, 0])
            self.display.blit(self.heart, [96, 0])
        elif self.counter == 2:
            self.display.blit(self.heart, [0, 0])
            self.display.blit(self.heart, [48, 0])
        elif self.counter == 1:
            self.display.blit(self.heart, [0, 0])
        else:
            text = font.render(f"GAME OVER", True, RED)
            screen.blit(text, [325, 400])
            now = g.time.get_ticks()

#########################################################

g.init()

# game dependents
screen = g.display.set_mode(SIZE)
g.display.set_caption("Jame Scene")
clock = g.time.Clock()
GUNSOUND = g.mixer.Sound('revolvershot.ogg')

# create enemas

enema_list = []
for call in range(4):
    enema_list.append(enema(screen, 950, 690 - (call * 200), 0, 0))

bullet_list = []
for call in range(4):
    bullet_list.append(bullet(screen, 885, 745 - (call * 200)))
    GUNSOUND.play()

dude = man(screen, 0, 0)

g.mixer.music.load('OnceUponATime.ogg')
g.mixer.music.set_endevent(g.constants.USEREVENT)
g.mixer.music.play()

# game
running = True
while running:

    for event in g.event.get():
        if event.type == g.QUIT:
            running = False
        if event.type == g.KEYDOWN:
            if event.key == g.K_DOWN:
                if dude.y <= 599:
                    dude.y += 200
            elif event.key == g.K_UP:
                if dude.y >=199:
                    dude.y -= 200

    desert = g.image.load('western.jpg')
    desert = g.transform.scale(desert, [1100, 850])
    screen.blit(desert, [0, 0])

    for enema in enema_list:
        enema.draw_man()

    for bullet in bullet_list:
        bullet.draw_bullet()
        bullet.shoot_bullet()
        if dude.is_collided(bullet):
            running = False

    if dude.dead:
        running = False

    dude.draw_good_man()

    g.display.flip()

    clock.tick(FPS)