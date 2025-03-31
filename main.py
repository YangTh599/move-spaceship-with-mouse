import pygame, sys
import random
import math
import os
from os.path import join
from random import randint as rnd
from pygame.time import delay as slp

from colors import *
from pygame_config import *
import classes_and_objects.shapes as shapes
import classes_and_objects.boxes as boxes

def init_game():
    """Initiates Pygame, Pygame.font, and sets the Screen window and caption"""
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption(PYGAME_CAPTION) # Window Caption

    #Pygame Window
    window = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    return window

# Draw Function to update graphics
def draw(window,bg,player):
    """DRAW FUNCTION | allows screen graphics to be added"""
    #BACKGROUND
    # window.fill(WHITE) # 15
    window.blit(bg, [0,0])

    #FOREGROUND
    
    mouse_pos = pygame.mouse.get_pos()

    window.blit(player, [mouse_pos[0] - player.get_width()//2, mouse_pos[1] - player.get_height() // 2])

    #UPDATE DISPLAY
    pygame.display.update()

def handle_events():
    """Handles any pygame event such as key input"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # QUIT
            return False
    
    return True

def main(): # MAIN FUNCTION
    """Main Function : main"""
    window = init_game()
    clock = pygame.time.Clock()
    # ADD ALL OBJECTS/CLASSES BELOW HERE
    background_image = pygame.image.load("assets/saturn_family1.jpg").convert()
    player_image = pygame.image.load("assets/player.png").convert()
    player_image.set_colorkey(BLACK)
    
    # ADD ALL OBJECTS/CLASSES ABOVE HERE
    run = True
    while run: # run set to true, program runs while run is true.

        clock.tick(FPS) # FPS Tick

        run = handle_events()
        

        
        draw(window,background_image,player_image) # UPDATES SCREEN

    pygame.quit()
    sys.quit()
    quit()
# ADD CLASSES HERE



# ADD CLASSES ABOVE
if __name__ == "__main__": 
    main()

