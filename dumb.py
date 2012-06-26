import pygame
from pygame.locals import *
import platform
import background
import game

def keydownfunc(event):
    if event.key == K_UP:
        

def main():
    bg = Background('grassybg.bmp', floor_height=720)
    objs = {
        'sprite' : Sprite()
    }
    
    funcs = {
        KEYDOWN : (
            lamda x:
                
        )
    }
    game = Game((900, 900), bg, objs, funcs)
    