import pygame
import sceneobject
import background

class TwoLayerBackground(background.Background):
    def __init__(self, staticbg = None, dynamicfg = None, rect=(0,0,512,256), color=None, floor_height=None, terrain_map=None, static_pos=(None, None)):
        background.Background.__init__(self, dynamicfg, rect, color, floor_height)
        # This line performs the following tests: if staticbg was provided, use that. Else, if color was provided, use a new surface filled with that color. Else, use a new surface filled with deep gray.
        self.staticimage = self.image = pygame.image.load(staticbg).convert_alpha() if staticbg else utils.ColoredSurface((width,height),color) if color else utils.ColoredSurface((width,height),(10,10,10), terrain_map)
        self.static_pos = static_pos
        
    def draw(self, surface):
        surface.blit(self.staticimage, (self.static_pos[0] or 0, self.static_pos[1] or 0), pygame.Rect(0,0,self.width,self.height))
        surface.blit(self.image, (0,0), pygame.Rect(self.x,self.y,self.width,self.height))
