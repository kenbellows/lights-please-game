import pygame
import sys
import os
import lightspleasegame
import gamelib.game
import gamelib.scene
import gamelib.sceneobject
import gamelib.charactersprite
import gamelib.platform
import gamelib.terrain
import gamelib.twolayerbackground
from gamelib.action import Action

WIDTH = 900
HEIGHT = 600
STATIC_BGFILE = 'static_sky.bmp'
DYNAMIC_FGFILE = 'grassy_fg.bmp'
STATICX = 3200 - WIDTH
STATICY = 0
BGSTARTX = 0
BGSTARTY = 800 - HEIGHT
FLOORHEIGHT = 500
CHRSPRITESHEET = 'simple_sprite_sheet.bmp'
CHRWIDTH = 100
CHRHEIGHT = 125
CHRJUMPHEIGHT = 200

t_points = [ (0,0), (80,0), (175,30), (260,10), (330,40), (575,40), (670,0), (990,0), (1120,50), (1220,10), (1315,0), (2050,0), (2060,50), (3200,50) ]
TERRAIN_POINTS = []
for point in t_points:
    TERRAIN_POINTS.append((point[0],FLOORHEIGHT-point[1]))

TERRAIN_MAP = gamelib.terrain.Terrain(TERRAIN_POINTS)


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
            'TYPE'            : 'TWO_LAYER_IMAGE',
            'STATIC_FILENAME' : STATIC_BGFILE,
            'STATICX'         : STATICX,
            'STATICY'         : STATICY,
            'FILENAME'        : DYNAMIC_FGFILE,
            'STARTX'          : BGSTARTX,
            'STARTY'          : BGSTARTY,
            'WIDTH'           : WIDTH,
            'HEIGHT'          : HEIGHT,
    }
    
    gameobjects = [
        { # Main CharacterSprite
            'CONSTRUCTOR' : gamelib.charactersprite.CharacterSprite,
            'filename'    : CHRSPRITESHEET,
            'actions'     : actions, 
            'width'       : CHRWIDTH,
            'height'      : CHRHEIGHT,
            'pos'         : TERRAIN_MAP.groundtest((BGSTARTX+30,FLOOR_HEIGHT))[1]-CHRHEIGHT,
            'jumpheight'  : CHRJUMPHEIGHT,
            'terrain'     : TERRAIN_MAP,
        },
    ]
    
    maingame = lightspleasegame.LightsPleaseGame((WIDTH,HEIGHT), bg_info, objects=gameobjects)
    maingame.run()
    

if __name__ == "__main__":
    main()