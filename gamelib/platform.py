import pygame
import sceneobject

class Platform(sceneobject.SceneObject):
    def __init__(self, filename, (x,y), intersect_depth):
        sceneobject.SceneObject.__init__(self,filename,(x,y))
        self.intersect_depth = intersect_depth
    
    def intersect(self, (x,y)):
        BGPINK = (255, 0, 255, 255)
        colorsurf = pygame.Surface((self.image.get_width(), self.image.get_height()))
        colorsurf.fill(BGPINK)
        colorsurf.blit(self.image, (0,0))
        
        count = 0
        x = BGPINK
        while x == BGPINK:
            count += 1
            x = colorsurf.get_at((count,self.intersect_depth))
        leftbound = count
        
        count = self.image.get_width()
        x = BGPINK
        while x == BGPINK:
            count -= 1
            x = colorsurf.get_at((count,self.intersect_depth))
        rightbound = count
        
        return x >= leftbound and x <= rightbound and y <= self.intersect_depth