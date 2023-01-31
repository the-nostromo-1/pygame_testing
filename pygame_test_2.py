#!/usr/bin/env python3

# from https://realpython.com/pygame-a-primer/#background-and-setup
# following the step by step insstructions for the sites pygame tutorial
# I added many of my own notes(comments) as well
# David J Tinley
# 01/30/2023

# importing pygame
import pygame
# importing rand fucntion
import random

# importing pygame.locals for easier access to key coordinates
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT
)

# define constants for the screen width and heigth
SCREEN_WIDTH = 800
SCREEN_HEIGTH = 600

# Define a Player object by extending pygame.sprite.Sprite
# The surface drawn on the screen is now an attribute of 'player'


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        # defining and initializing and setting dimensions of .surf for this class
        self.surf = pygame.Surface((75, 25))
        # making self surface white
        self.surf.fill((251, 73, 52))
        # defining and initializing .rect for this class
        self.rect = self.surf.get_rect()

    # Move the sprite based on user keypresses
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            # moving up the y axis
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            # moving down the y axis
            self.rect.move_ip(0, 5)
        if pressed_keys[K_RIGHT]:
            # moving right on the x axis
            self.rect.move_ip(5, 0)
        if pressed_keys[K_LEFT]:
            # moving left on the x axis
            self.rect.move_ip(-5, 0)

        # keeping the player on the screen by changing the coordinates of
        # .top, .bottom, .left, .right values of the self.rect
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGTH:
            self.rect.bottom = SCREEN_HEIGTH

# Define the enemy object by extending pygame.sprite.Sprite
# The surface you draw on the screen is now an attribute of 'enemy'


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        # defining and initializing and setting dimensions of .surf for this class
        self.surf = pygame.Surface((25, 15))
        # making self surface orange
        self.surf.fill((254, 128, 25))
        # defining and initializing .rect for this class
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGTH)
            )
        )
        self.speed = random.randint(5, 20)

    # updating self
    def update(self):
        # move the sprite based on speed
        # remove the sprite when it passes the left edge of the screen
        # the sprites only move horizontally from right to left
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()


# instantiate player. Right now, this is just a rectangle.
player = Player()

# initialize pygame
pygame.init()

# create the screen object
# the size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
# pygame.display.set_mode returns a "Surface" object
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGTH))

# create groups to hold enemy sprites and all sprites
# - enemies is used for collision detection and position updates
# - all_sprites is used for rendering
enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# running variable
running = True

# main game loop
while running:
    # look at every event in the game
    for event in pygame.event.get():
        # if user hits a key
        if event.type == KEYDOWN:
            # if key is the escape key stop loop
            if event.key == K_ESCAPE:
                running = False
        # else if user closes window
        elif event.type == QUIT:
            running = False

        # Get the set of keys pressed and check for user input
        pressed_keys = pygame.key.get_pressed()
        # Update the player sprite based on user keypresses
        player.update(pressed_keys)

        # fill screen with color
        screen.fill((29, 32, 33))

        # draw all sprites
        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)

        # flip everything to the display
        pygame.display.flip()

        # create a surface and pass in a tuple containing its length and width
        # my_surface = pygame.Surface((50, 50))
        # give the surface a color to separate it from the background
        # my_surface.fill((251, 73, 52))
        # my_rectangle = my_surface.get_rect()

        # .blit() stands for Block Transfer and .blit() is how you copy the contents of one Surface to another.
        # .blit() takes two arguments: the Surface to draw and the location on the other Surface to draw the new one
        # this line says "Draw surf onto the screen at the center"
        # screen.blit(my_surface, (SCREEN_WIDTH/2, SCREEN_HEIGTH/2))
        # pygame.display.flip()

        # put the center of surf at the center of the display
        # surface_center = (
        #     (SCREEN_WIDTH - my_surface.get_width())/2,
        #     (SCREEN_HEIGTH - my_surface.get_height())/2
        # )

        # draw player.surf at the new coordinates
        # screen.blit(player.surf, player.rect)
