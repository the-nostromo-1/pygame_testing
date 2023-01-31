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
    RLEACCEL,
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

# initialize pygame
pygame.init()

# Setup for sounds. Defaults are good.
# must call before pygame.init if you want to change defaults
pygame.mixer.init()

# create the screen object
# the size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
# pygame.display.set_mode returns a "Surface" object
# must be initialized before any images are loaded
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGTH))

# Load and play background music
# Sound source: http://ccmixter.org/files/Apoxode/59262
# License: https://creativecommons.org/licenses/by/3.0/
pygame.mixer.music.load(
    "/Users/djt/Desktop/testing_folder/pygame_testing/sound_assets/Apoxode.mp3")
# loop music infinitely by putting "loops=-1"
pygame.mixer.music.play(loops=-1)


# Load all sound files
# Sound sources: Jon Fincher
move_up_sound = pygame.mixer.Sound(
    "/Users/djt/Desktop/testing_folder/pygame_testing/sound_assets/Rising_putter.oga")
move_down_sound = pygame.mixer.Sound(
    "/Users/djt/Desktop/testing_folder/pygame_testing/sound_assets/Falling_putter.oga")
collision_sound = pygame.mixer.Sound(
    "/Users/djt/Desktop/testing_folder/pygame_testing/sound_assets/Collision.oga")

# Define a Player object by extending pygame.sprite.Sprite
# The surface drawn on the screen is now an attribute of 'player'


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        # defining and initializing and setting dimensions of .surf for this class
        # self.surf = pygame.Surface((75, 25))
        # making self surface colored
        # self.surf.fill((251, 73, 52))
        # loading image for player character
        self.surf = pygame.image.load(
            "/Users/djt/Desktop/testing_folder/pygame_testing/image_assets/jet.png").convert()
        # defining color that pygame will render as transparent
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        # defining and initializing .rect for this class
        self.rect = self.surf.get_rect()

    # Move the sprite based on user keypresses
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            # moving up the y axis
            self.rect.move_ip(0, -5)
            # playing sound when event happens
            move_up_sound.play()
        if pressed_keys[K_DOWN]:
            # moving down the y axis
            self.rect.move_ip(0, 5)
            # playing sound when event happens
            move_down_sound.play()
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
        # self.surf = pygame.Surface((25, 15))
        # making self surface orange
        # self.surf.fill((254, 128, 25))
        # loading image for the enemies
        self.surf = pygame.image.load(
            "/Users/djt/Desktop/testing_folder/pygame_testing/image_assets/missile.png").convert()
        # definig color that pygame will render as transparent
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
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

# Define the cloud object by extending pygame.sprite.Sprite
# Use an image for a better-looking sprite


class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        super(Cloud, self).__init__()
        self.surf = pygame.image.load(
            "/Users/djt/Desktop/testing_folder/pygame_testing/image_assets/cloud.png").convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGTH)
            )
        )
        self.speed = random.randint(2, 3)

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()


# instantiate player. Right now, this is just a rectangle.
player = Player()

# Setup the clock for a decent framerate
clock = pygame.time.Clock()


# create groups to hold enemy sprites and all sprites
# - enemies is used for collision detection and position updates
# - all_sprites is used for rendering
enemies = pygame.sprite.Group()
clouds = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# create a custom event for adding a new enemy
# pygame defines events internally as integers, so you need to define a new event with a unique integer.
# the last event pygame reserves is called USEREVENT,
# so defining ADDENEMY = pygame.USEREVENT + 1 ensures it’s unique.
ADDENEMY = pygame.USEREVENT + 1
ADDCLOUD = pygame.USEREVENT + 2
# sets timer to call event every 250 milliseconds
pygame.time.set_timer(ADDENEMY, 250)
pygame.time.set_timer(ADDCLOUD, 1000)

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

        # add enemy
        elif event.type == ADDENEMY:
            # create the new enemy and add it to sprite groups
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)

        # add cloud
        elif event.type == ADDCLOUD:
            new_cloud = Cloud()
            clouds.add(new_cloud)
            all_sprites.add(new_cloud)

    # update enemy position
    enemies.update()
    # update cloud position
    clouds.update()

    # Get the set of keys pressed and check for user input
    pressed_keys = pygame.key.get_pressed()
    # Update the player sprite based on user keypresses
    player.update(pressed_keys)

    # fill screen with color
    screen.fill((0, 100, 200))

    # draw all sprites
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    # check if any enemies have collided with the player
    if pygame.sprite.spritecollideany(player, enemies):
        # if collision, kill player
        player.kill()
        # Stop any moving sounds and play the collision sound
        move_up_sound.stop()
        move_down_sound.stop()
        collision_sound.play()
        # quit game
        running = False

    # flip everything to the display
    pygame.display.flip()

    # Ensure program maintains a rate of 30 frames per second
    clock.tick(30)

# stop all music after loop ends
pygame.mixer.music.stop()
pygame.mixer.quit()
