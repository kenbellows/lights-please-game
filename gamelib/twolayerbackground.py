import pygame
import sceneobject
import background

class TwoLayerBackground(background.Background):
    def __init__(self, staticbg = None, dynamicbg = None, (x, y, width, height)=(0,0,512,256), color=None, floor_height=None):
        background.Background.__init__(self, dynamicbg, (x, y, width, height), color, floor_height)
        # This line performs the following tests: if staticbg was provided, use that. Else, if color was provided, use a new surface filled with that color. Else, use a new surface filled with deep gray.
        self.staticimage = staticbg if staticbg else utils.ColoredSurface((width,height),color) if color else utils.ColoredSurface((width,height),(10,10,10))

        
    def draw(self, surface):
        surface.blit(self.staticimage, (0,0), pygame.Rect(0,0,self.width,self.height))
        surface.blit(self.image, (0,0), pygame.Rect(self.x,self.y,self.width,self.height))
