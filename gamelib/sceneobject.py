import pygame


class SceneObject(pygame.sprite.Sprite):
    def __init__(self, args):
        
        pygame.sprite.Sprite.__init__(self)
        self.x = args['pos'][0]
        self.y = args['pos'][1]
        if args['filename'] != None:
            self.image = pygame.image.load(args['filename']).convert_alpha()
        else:
            self.image = None
        self.init_pos = self.x, self.y
        self.terrain = args['terrain']
    def pos(self):
        return (self.x, self.y)
    
    def move(self, (x,y)=(10,0)):
        self.x += x
        self.y += y
    
    def moveto(self, (x,y)):
        self.x = x
        self.y = y
        
    def reset(self):
        self.x, self.y = self.init_pos

    def draw(self, surface):
        surface.blit(self.image, self.pos(), pygame.Rect(0,0,self.width,self.height))
        
    def drawable(self):
        return self.image
    
    def handle(self, event):
        pass
    
    def update(self):
        pass
