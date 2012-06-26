import pygame
import scene
import background

class Game:
    def __init__(self, (width, height), bg_info, objects=[], functions={}):
        pygame.init()
        self.screen = pygame.display.set_mode((width,height))
        self.width = width
        self.height = height
        self.running = True
        self.functions = functions
        
        self.bg = None
        if bg_info['TYPE'] == 'SOLID':
            self.bg = background.Background(None, (0,0, bg_info['WIDTH'], bg_info['HEIGHT']), bg_info['COLOR'], bg_info['FLOORHEIGHT'])
        elif bg_info['TYPE'] == 'IMAGE':
            self.bg = background.Background(bg_info['FILENAME'], (bg_info['STARTX'],bg_info['STARTY'],bg_info['WIDTH'],bg_info['HEIGHT']), floor_height=bg_info['FLOORHEIGHT'])
        self.objects = []
        
        for item in objects:
            self.objects.append(item['CONSTRUCTOR'](item))
        
        
        self.scene = scene.Scene(self.bg, self.objects, bg_type=bg_info['TYPE'])
    
    def register_event(type, response_function):
        self.functions[type] = response_function
    
    def update(self):
        pass
    
    def main_loop_iteration(self):
        for event in pygame.event.get():
            if   event.type == pygame.QUIT:
                self.running = False
                return
            elif event.type in self.functions:
                self.functions[event.type](event)
            else:
                for obj in self.objects:
                    obj.handle(event)
        for obj in self.objects:
            obj.update()
        self.update()
        self.screen.blit(self.scene.drawable(), (0,0))
        pygame.display.flip()
    
    def run(self):
        print "Entering the game loop.\n\n\nReady, Go!\n\n"
        while self.running:
            self.main_loop_iteration()
