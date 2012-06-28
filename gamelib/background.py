import pygame
import sceneobject
import terrain

class Background(sceneobject.SceneObject):
    def __init__(self, filename=None, (x, y, width, height)=(0,0,512,256), color=None, floor_height=None, terrain_map=None):
        so_args = {'pos':(x,y), 'filename':filename}
        sceneobject.SceneObject.__init__(self,so_args)
        self.color = color
        self.width = width
        self.height = height
        self.floor_height = floor_height if floor_height and not terrain_map else height/2
        self.terrain_map = terrain_map if terrain_map else terrain.Terrain([(0,self.floor_height), (self.width,self.floor_height)])
        
    def drawable(self):
        currscene = pygame.Surface((self.width,self.height))
        self.draw(currscene)
        return currscene
        
    def draw(self, surface):
        if self.image:
            surface.blit(self.image, (0,0), pygame.Rect(self.x,self.y,self.width,self.height))
        elif self.color:
            self.blit(utils.ColoredSurface((self.width,self.height),self.color), (0,0), pygame.Rect(self.x,self.y,self.width,self.height))
    
    def ground_test(self, point):
        return self.terrain_map.ground_test(point)