import pygame
import gamelib.game
import gamelib.charactersprite

class LightsPleaseGame(gamelib.game.Game):
    def __init__(self, (width, height), bg_info, objects=[], functions={}):
        self.hero = None
        gamelib.game.Game.__init__(self, (width, height), bg_info, objects, functions)
        for obj in self.objects:
            if isinstance(obj, gamelib.charactersprite.CharacterSprite):
                self.hero = obj
                break
    
    def update(self):
        move_distance_factor = 0.85
        if self.bg:
            if   self.bg.x + self.bg.width > self.bg.image.get_rect().width:
                self.bg.moveto((self.bg.image.get_rect().width-self.bg.width-1, self.bg.y))
            elif self.bg.x < 0:
                self.bg.moveto((0, self.bg.y))
            
            if self.hero:
                if   self.hero.x > self.bg.width*move_distance_factor:
                    self.hero.moveto((self.width*move_distance_factor, self.hero.y))
                    self.bg.move((self.hero.walk_step * (self.hero.fast_factor if self.hero.state['running'] else 1), 0))
                elif self.hero.x < self.bg.width*(1-move_distance_factor) and self.bg.x + self.bg.width < self.bg.image.get_rect().width:
                    self.hero.moveto((self.width*(1-move_distance_factor), self.hero.y))
                    self.bg.move((-self.hero.walk_step * (self.hero.fast_factor if self.hero.state['running'] else 1), 0))