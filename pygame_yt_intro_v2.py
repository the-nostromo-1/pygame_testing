#!/usr/bin/env python3

#
# Restarting Youtube tutorial using provided assets
# David J Tinley
# 02/01/2023
#

import pygame
from sys import exit

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGTH = 400
FRAME_RATE = 60

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGTH))
clock = pygame.time.Clock()

testFont = pygame.font.Font(
    "/Users/djt/Desktop/pygame_testing/font_assets/Pixeltype.ttf", 50)
textSurface = testFont.render('My Game', False, (254, 128, 25))

background = pygame.image.load(
    "/Users/djt/Desktop/pygame_testing/image_assets/sky.png").convert_alpha()
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGTH))

grass = pygame.image.load(
    "/Users/djt/Desktop/pygame_testing/image_assets/ground.png")
grass = pygame.transform.scale(grass, (SCREEN_WIDTH, 200))

snail = pygame.image.load(
    "/Users/djt/Desktop/pygame_testing/image_assets/snail/snail1.png").convert_alpha()
snailXPos = 700

player = pygame.image.load(
    "/Users/djt/Desktop/pygame_testing/image_assets/Player/player_walk_1.png").convert_alpha()
playerRect = player.get_rect(midbottom=(SCREEN_WIDTH/3, 325))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    screen.blit(background, (0, 0))
    screen.blit(grass, (0, 325))
    screen.blit(textSurface, (350, 10))
    snailXPos -= 0.75
    if snailXPos < (-50):
        snailXPos = 700
    screen.blit(snail, (snailXPos, 295))
    screen.blit(player, playerRect)

    pygame.display.update()
    clock.tick(FRAME_RATE)
