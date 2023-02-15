# As in the menus we'll need rects to make it work properly, we'll need text too. In our whole game we will, so we need to learn how to display it correctly. Let's get into it!

# First, we import and init the PyGame module as pg to write less. Remember, the less we write, the better. #TLWWTB
import pygame as pg
pg.init()

# Window settings.
screenSize = (1280, 720) # Resolution.
screen = pg.display.set_mode(screenSize) # Display window.
pg.display.set_caption("Display text in PyGame") # Caption.

# Variables
fontColor = (228, 143, 143) # Color of our text.
font = pg.font.Font("sourceserifpro.ttf", 80) # Font and size of our text.
text = font.render("Text has been displayed correctly! :D", True, fontColor) # Before displaying text, you need to render it, to make it true and appoint a color.
background = (154, 255, 218) # Window's background color.

# Main loop of the game.
finish = False
while(finish == False):
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finish = True
    
    screen.fill(background) # Fill all the window surface with the color we gave.
    screen.blit(text, (130, 270)) # Draws the text (already rendered) and we give it paddings (top and left). 
    pg.display.update() # Updates the screen surface.


#Note: Comment everything and uncomment the following line to see ALL the available fonts for PyGame
#pg.font.get_fonts()