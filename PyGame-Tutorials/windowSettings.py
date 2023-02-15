# We can modify some values to make our window look better. We can change the caption (title of the window) and icon.

import pygame
pygame.init()

# Screen.
screenSize = (1280, 720)
screen = pygame.display.set_mode(screenSize)

# Change caption (window title).
pygame.display.set_caption("Caption taken!")

# Change icon of the window.
pygame.display.set_icon() # Between the parenthesis we'll put the name of the icon or path to it.

# Main loop + Close program.
finishProgram = False
while(finishProgram == False): 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finishProgram = True