#!/usr/bin/env python3

import pygame
# imports system exit function
from sys import exit
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
pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGTH = 600
FRAME_RATE = 60

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGTH))
pygame.display.set_caption('King Tiger')
clock = pygame.time.Clock()
test_font = pygame.font.Font(
    "/Users/djt/Desktop/testing_folder/pygame_testing/font_assets/OldLondon.ttf", 50)

# Background
background = pygame.image.load(
    "/Users/djt/Desktop/testing_folder/pygame_testing/image_assets/tank_background.png").convert_alpha()
# stretching image to display size
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGTH))
#
# King Tiger tank
kingTiger = pygame.image.load(
    "/Users/djt/Desktop/testing_folder/pygame_testing/image_assets/Tiger-II_preview.png").convert_alpha()
kingTiger = pygame.transform.scale(kingTiger, (50, 100))
# kingTiger.set_colorkey((0, 0, 0))
#
# Text surface
text_surface = test_font.render("King Tiger", False, (254, 128, 25))
#
# T34 tank
t34 = pygame.image.load(
    "/Users/djt/Desktop/testing_folder/pygame_testing/image_assets/T34_preview.png").convert_alpha()
t34 = pygame.transform.scale(t34, (40, 85))
# t34.set_colorkey((0, 0, 0))
t34XPos = 400
t34YPos = 0
t34Speed = 1
#

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(background, (0, 0))
    screen.blit(kingTiger, (SCREEN_WIDTH/2, SCREEN_HEIGTH/2))
    screen.blit(text_surface, (0, 0))
    t34YPos += (t34Speed)
    if t34YPos >= SCREEN_HEIGTH + 5:
        t34YPos = 0
    screen.blit(t34, (t34XPos, t34YPos))
    pygame.display.update()
    clock.tick(FRAME_RATE)
