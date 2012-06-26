import pygame
import sys
import os
import gamelib.game
import gamelib.scene
import gamelib.sceneobject
import gamelib.charactersprite
import gamelib.platform
import lightspleasegame
from gamelib.action import Action

WIDTH = 900
HEIGHT = 600
BGFILE = 'grassybg.bmp'
BGSTARTX = 0
BGSTARTY = 200
FLOORHEIGHT = 700
CHRSPRITESHEET = 'simple_sprite_sheet.bmp'
CHRWIDTH = 100
CHRHEIGHT = 125
CHRJUMPHEIGHT = 400
def main():

    actions = {
            'STAND'       : Action(0, 1),
            'WALK'        : Action(1, 4),
            'RUN'         : Action(1, 4),
            'JUMP'        : Action(2, 7),
            'FALL'        : Action(3, 2),
            'FALL_FAST'   : Action(4, 2),
            'LAND'        : Action(5, 4),
    }
    
    bg_info = {
            'TYPE'        : 'IMAGE',
            'FILENAME'    : BGFILE,
            'STARTX'      : BGSTARTX,
            'STARTY'      : BGSTARTY,
            'WIDTH'       : WIDTH,
            'HEIGHT'      : HEIGHT,
            'FLOORHEIGHT' : FLOORHEIGHT,
    }
    
    gameobjects = [
        { # Main CharacterSprite
            'CONSTRUCTOR' : gamelib.charactersprite.CharacterSprite,
            'FILENAME'    : CHRSPRITESHEET,
            'ACTIONS'     : actions, 
            'WIDTH'       : CHRWIDTH,
            'HEIGHT'      : CHRHEIGHT,
            'STARTPOS'    : (BGSTARTX+30, FLOORHEIGHT-BGSTARTY-CHRHEIGHT), 
            'JUMPHEIGHT'  : CHRJUMPHEIGHT,
        },
    ]
    
    maingame = lightspleasegame.LightsPleaseGame((WIDTH,HEIGHT), bg_info, objects=gameobjects)
    maingame.run()
    

if __name__ == "__main__":
    main()