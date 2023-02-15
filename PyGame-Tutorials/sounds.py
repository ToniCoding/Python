# A game without music is not a good game nowadays so here's how to play your music! You can play an specific sound.
# Import and initialize PyGame module.
import pygame as pg
pg.init()

# Screen settings.
ScreenSize = (1280, 720)
screen = pg.display.set_mode(ScreenSize)
pg.display.set_caption("Play sounds!")

# Sounds loader and player.
mySound = "mySound.wav" # This defines our sound.
mySound2 = "mySound2.wav"
playIt1 = pg.mixer.Sound(mySound) # Now, we create variables to play the sound when it's called.
playIt2 = pg.mixer.Sound(mySound2)

# With channels we can create sounds that'll play at the same time. Every sound has its own sound channel.
pg.mixer.Channel(0).play(playIt1, -1) # -1 to play it continously. Next to it, a .play to play the sound.
pg.mixer.Channel(1).play(playIt2, -1) # Syntax is: creationOfTheChannel(N).playTheSound(whichSound, times)


# Main loop.
finishProgram = False
while(finishProgram == False): 
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finishProgram = True