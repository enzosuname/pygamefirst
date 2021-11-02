import pygame
from settings import *

# create color constants
WHITE = (255, 255, 255)
RED = (87, 9, 9)
GREEN = (12, 148, 37)
BLUE = (2, 0, 94)
BLACK = (0, 0, 0)

# width by height
FPS = 60
DISPLAY_WIDTH = 1000
DISPLAY_HEIGHT = 800

# Player
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50

# Game Layout
LAYOUT = ['11111111111111111111',
          '10000000000000000001',
          '10000000000000000001',
          '10000000000000000001',
          '10000000000000000001',
          '10000000000000000001',
          '10000000000000000001',
          '10000000000000000001',
          '10000000000000000001',
          '11111111111111111111', ]

WALL_BRICK_WIDTH = DISPLAY_WIDTH // len(LAYOUT[0])
WALL_BRICK_HEIGHT = DISPLAY_HEIGHT // len(LAYOUT)


class Player:
    def __init__(self, display, color, x, y, width, height):
        self.display = display
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velo = 5
        self.x_velo = 0
        self.y_velo = 3
        self.jumping = False
        self.falling = False
        self.y_counter = 0
        self.jump_height = int(self.height * 0.6)

    def draw_player(self):
        pygame.draw.rect(self.display, self.color,
                         (self.x, self.y, self.width, self.height))

    def player_keys(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x_velo = -1 * self.velo
        elif keys[pygame.K_RIGHT]:
            self.x_velo = self.velo
        else:
            self.x_velo = 0

        if keys[pygame.K_SPACE] and self.jumping is False and self.falling is False:
            self.y_counter = 0
            self.jumping = True



        #set the x veloc based on key presses

    def move_player(self):
        self.x += self.x_velo

        if self.x < WALL_BRICK_WIDTH:
            self.x = WALL_BRICK_WIDTH
        elif self.x + self.width > DISPLAY_WIDTH - WALL_BRICK_WIDTH:
            self.x = DISPLAY_WIDTH - WALL_BRICK_WIDTH - self.width

        # player movement is jumping, going up

        if self.jumping:
            self.y_counter += 1
            self.y -= self.y_velo

            if self.y_counter >= self.jump_height:
                self.jumping = False
                self.falling = True

        # player movement is falling, going down

        if self.falling:
            if self.y + self.height >= DISPLAY_HEIGHT - WALL_BRICK_HEIGHT:
                self.y = DISPLAY_HEIGHT - WALL_BRICK_HEIGHT - self.height
                self.falling = False
            else:
                self.y += self.y_velo

    def control_player(self):
        # call all player movement functions
        self.player_keys()
        self.draw_player()
        self.move_player()


class Ball:
    def __init__(self, display, color, x, y, width, height):
        self.display = display
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height


class Walls():
    def __init__(self, display, color, x, y, width, height):
        self.display = display
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def make_walls(self):
        pygame.draw.rect(self.display, self.color,
                         (self.x, self.y, self.width, self.height))


pygame.init()

screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption("Game Title")

clock = pygame.time.Clock()
player = Player(screen, BLUE,
                WALL_BRICK_WIDTH * 2,
                DISPLAY_HEIGHT - WALL_BRICK_HEIGHT - PLAYER_HEIGHT,
                PLAYER_WIDTH, PLAYER_HEIGHT)

wall_blocks = []
for row in range(len(LAYOUT)):
    y_loc = row * WALL_BRICK_HEIGHT

    for col in range(len(LAYOUT[0])):
        x_loc = col * WALL_BRICK_WIDTH

        if LAYOUT[row][col] == '1':
            brick = Walls(screen, RED, x_loc, y_loc, WALL_BRICK_WIDTH, WALL_BRICK_HEIGHT)
            wall_blocks.append(brick)

running = True

while running:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    for block in wall_blocks:
        block.make_walls()

    player.control_player()

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
