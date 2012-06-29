import pygame
import sceneobject
import terrain

class Background(sceneobject.SceneObject):
    def __init__(self, filename=None, rect=(0,0,512,256), color=None):
        (x, y, width, height) = rect
        so_args = {'pos':(x,y), 'filename':filename, 'terrain':None}
        sceneobject.SceneObject.__init__(self,so_args)
        self.color = color
        self.width = width
        self.height = height
        
    def drawable(self):
        currscene = pygame.Surface((self.width,self.height))
        self.draw(currscene)
        return currscene
        
    def draw(self, surface):
        if self.image:
            surface.blit(self.image, (0,0), pygame.Rect(self.x,self.y,self.width,self.height))
        elif self.color:
            self.blit(utils.ColoredSurface((self.width,self.height),self.color), (0,0), pygame.Rect(self.x,self.y,self.width,self.height))