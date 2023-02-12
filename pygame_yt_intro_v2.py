#!/usr/bin/env python3

#
# Restarting YouTube tutorial using provided assets
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

scoreFont = pygame.font.Font("/Users/djt/Desktop/pyGameTesting/font_assets/Pixeltype.ttf", 50)
scoreSurface = scoreFont.render('My Game', False, (64, 64, 64))
scoreRect = scoreSurface.get_rect(center=(SCREEN_WIDTH/2, 50))

background = pygame.image.load("/Users/djt/Desktop/pyGameTesting/image_assets/sky.png").convert_alpha()
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGTH))

grass = pygame.image.load("/Users/djt/Desktop/pyGameTesting/image_assets/ground.png")
grass = pygame.transform.scale(grass, (SCREEN_WIDTH, 200))

snail = pygame.image.load("/Users/djt/Desktop/pyGameTesting/image_assets/snail/snail1.png").convert_alpha()
snailRect = snail.get_rect(bottomright=(SCREEN_WIDTH - 100, 325))
snailXPos = 700

player = pygame.image.load("/Users/djt/Desktop/pyGameTesting/image_assets/Player/player_walk_1.png").convert_alpha()
playerRect = player.get_rect(midbottom=(SCREEN_WIDTH/3, 325))
playerGravity = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        if event.type == pygame.KEYDOWN:
            if playerRect.bottom >= 325: # forces player to be back on ground
                # before they can jump again
                playerGravity = -20

    screen.blit(background, (0, 0))
    screen.blit(grass, (0, 325))
    pygame.draw.line(screen, 'Black', (0, 0), (SCREEN_WIDTH, SCREEN_HEIGTH))
    pygame.draw.rect(screen, '#c0e8ec', scoreRect)
    pygame.draw.rect(screen, '#c0e8ec', scoreRect, 10)
    screen.blit(scoreSurface, scoreRect)

    snailRect.x -= 1.75

    if snailRect.right <= 0:
        snailRect.left = SCREEN_WIDTH

    screen.blit(snail, snailRect)

    # print(playerRect.left)
    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_SPACE]:
    #     print("jump")

    # Player ################################################
    playerGravity += 1
    playerRect.y += playerGravity # simulating exponential gravity
    if playerRect.bottom >= 325:
        playerRect.bottom = 325
    screen.blit(player, playerRect)

    # .colliderect returns '0' or '1': 0 = no collision, 1 = collision
    # if playerRect.colliderect(snailRect):
    #     print("collision")

    # using mouse position in game
    # mousePos = pygame.mouse.get_pos()
    # checking if mouse position is colliding with the player
    # if playerRect.collidepoint(mousePos):
    # returns a bool of true or false if lmb, middle button, or rmb is pressed
    # print(pygame.mouse.get_pressed())

    pygame.display.update()
    clock.tick(FRAME_RATE)







#### EOF ####
