 # In a menu with buttons, we'll need to make some rects with properties in order to make it and for it, we have rects. Rects at the beggining may seem hard but with paying enought attention
 # to this will make rects easy peasy for you! Let's get into it. :) We'll make like a face with rectangles and different colors.

 #Note: I'll be commenting almost every line so I highly recommend you to read each comment.

# We'll start importing and initializing the module. The "as pg" means that instead of writting every single time "pygame.<function>" we'll just write pg.
import pygame as pg # Imports the module
pg.init() # Initialize it.

# Window summon, settings and configuration.
screenSize = (1280, 720) # Resolution of the screen, in this case HD (1280x720).
screenSummon = pg.display.set_mode(screenSize) # Variable to summon the screen.
pg.display.set_caption("get_Rect() Tutorial") # Sets the title of the window.

# Variables that will help us later.
redColor = (255, 0, 0) # RGB code for "Red".
greenColor = (0, 255, 0) # RGB code for "Green".
blueColor = (0, 0, 255) # RGB code for "Blue".
surfaceArea = (150, 250) # This will be the area of our rect.
surfaceArea2 = (250, 150) # 2nd surface area.
surfaceArea3 = (150, 250) # 3rd surface area but we can use the first surface area to save some lines. ;)
mySurface = pg.Surface(surfaceArea) # Creation of the surface, to be draw in the future.
mySurface2 = pg.Surface(surfaceArea2) # 2nd creation of the surface.
mySurface3 = pg.Surface(surfaceArea3) # 3rd creation of the surface. We can use again the first mySurface to save writting this lines.
displayMySurface = pg.display.set_mode(screenSize)
mySurface.fill(redColor) # Our rect / surface will be filled with the red color.
mySurface2.fill(greenColor) # This one, will be filled with green color.
mySurface3.fill(blueColor) # The last one, will be filled with blue color.
myRectPaddings = (250, 250) # Padding of the rect from the top left, expressed in pixels.
myRectPaddings2 = (500, 500) # 2x of padding to make it separate from the first rect.
myRectPaddings3 = (870, 250) # More padding than the others to make the face!
myRect = mySurface.get_rect(topleft = (myRectPaddings)) # Creates the rect with the parameter topleft that will receive the given parameters.
myRect2 = mySurface2.get_rect(topleft = (myRectPaddings2)) # Creates the 2nd rect with all the parameters.
myRect3 = mySurface3.get_rect(topleft = (myRectPaddings3)) # Creates the 3rd rect with all the parameters.

# Main loop of the game.
finish = False
while(finish == False):
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finish = True
        
        displayMySurface.blit(mySurface, myRect) # Finally, draws the rect in the surface.
        displayMySurface.blit(mySurface2, myRect2) # 2nd rect to see the result with different parameters.
        displayMySurface.blit(mySurface3, myRect3) # 3rd rect and the last one.
        pg.display.update() # Updates the screen to notice changes since the last window summon (the starting one in this case).