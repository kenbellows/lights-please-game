import pygame
import background
import terrain

class Scene:
    def __init__(self, bg=None, objects=None, bg_type=None):
        self.bg_type = bg_type if bg_type else 'SOLID'
        self.bg = bg if bg and bg_type else background.Background(color=(0,0,0))
        self.objects = objects
        
        
    def drawable(self):
        
        frame = pygame.Surface((self.bg.width,self.bg.height))
        
        # Fill the screen black
        if self.bg_type == 'SOLID':
            frame.fill(self.bg.color)
        else:
            frame.fill((0,0,0))
        
        # Add the scene's background first
        if self.bg:
            frame.blit(self.bg.drawable(), (0,0))
        
        # Then each of the scene objects
        for obj in self.objects:
            obj.draw(frame)
            #frame.blit(obj.drawable(), obj.pos())
        return frame
    
    