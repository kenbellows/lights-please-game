import pygame
import sceneobject

class Background(sceneobject.SceneObject):
    def __init__(self, filename=None, (x, y, width, height)=(0,0,512,256), color=None, floor_height=None):
        so_args = {'pos':(x,y), 'filename':filename}
        sceneobject.SceneObject.__init__(self,so_args)
        self.color = color
        self.width = width
        self.height = height
        self.floor_height = height/2 if floor_height == None else floor_height
        
    def drawable(self):
        currscene = pygame.Surface((self.width,self.height))
        self.draw(currscene)
        return currscene
        
    def draw(self, surface):
        if self.image == None and self.color == None: return
        
        if self.color:
            currscene = pygame.Surface((self.width,self.height))
            currscene.fill(self.color)
            if self.image:
                currscene.blit(self.image, (0,0), pygame.Rect(self.x,self.y,self.width,self.height))
                surface.blit(self.image, (0,0))
        elif self.image:
            surface.blit(self.image, (0,0), pygame.Rect(self.x,self.y,self.width,self.height))
