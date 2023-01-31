#!/usr/bin/env python3

# Import and initialize the pygame library
import pygame
pygame.init()
# Set up the drawing window
screen = pygame.display.set_mode([500, 500])

# Driver Code
# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((225, 225, 225))

    # Draw a solid blue circle in the center
    pygame.draw.circle(screen, (0, 0, 225), (250, 250), 75)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()

# Lines 4 and 5 import and initialize the pygame library. Without these lines, there is no pygame.

# Line 8 sets up your program’s display window. You provide either a list or a tuple that specifies the width and height of the window to create. This program uses a list to create a square window with 500 pixels on each side.

# Lines 11 and 12 set up a game loop to control when the program ends. You’ll cover game loops later on in this tutorial.

# Lines 15 to 17 scan and handle events within the game loop. You’ll get to events a bit later as well. In this case, the only event handled is pygame.QUIT, which occurs when the user clicks the window close button.

# Line 20 fills the window with a solid color. screen.fill() accepts either a list or tuple specifying the RGB values for the color. Since(255, 255, 255) was provided, the window is filled with white.

# Line 23 draws a circle in the window, using the following parameters:
#         screen: the window on which to draw
#         (0, 0, 255): a tuple containing RGB color values
#         (250, 250): a tuple specifying the center coordinates of the circle
#         75: the radius of the circle to draw in pixels

# Line 26 updates the contents of the display to the screen. Without this call, nothing appears in the window!

# Line 29 exits pygame. This only happens once the loop finishes.
