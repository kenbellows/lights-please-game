import pygame
from pygame.locals import *
import background

quit = False
pygame.init()
w,h = (1000,600)
display = pygame.display.set_mode((w,h))
sprite = background.Background('bg.bmp', (0,0,w,h))
#sprite = pygame.image.load('bg.bmp').convert_alpha()
x = 0
clock = pygame.time.Clock()

CLEAR = (255,0,255)
SHADE = (0,0,0)
SHADE_ALPHA = 100

pointlist = [(250,0), (350,0), (450, 480), (150, 480)]
intermediate = pygame.Surface((w,h))
intermediate.fill(CLEAR)
intermediate.set_colorkey(CLEAR)
pygame.draw.polygon(intermediate, SHADE, pointlist, 0)
intermediate.set_alpha(SHADE_ALPHA)

shader = pygame.Surface((w,h))

r=l=u=d=0
step = 3
while quit == False:
    clock.tick(60)
    
    # handle events (update game state)
    for event in pygame.event.get():
        if event.type == QUIT:
            quit = True
            break
        elif event.type == KEYDOWN:
            if   event.key == K_DOWN:
                d = 1
            elif event.key == K_UP:
                u = 1
            elif event.key == K_LEFT:
                l = 1
            elif event.key == K_RIGHT:
                r = 1
            elif event.key == K_LCTRL or event.key == K_RCTRL:
                step = 1
        elif event.type == KEYUP:
            if   event.key == K_DOWN:
                d = 0
            elif event.key == K_UP:
                u = 0
            elif event.key == K_LEFT:
                l = 0
            elif event.key == K_RIGHT:
                r = 0
            elif event.key == K_LCTRL or event.key == K_RCTRL:
                step = 3
                
    if d:
        sprite.move((0,step))
    if u:
        sprite.move((0,-step))
    if l:
        sprite.move((-step,0))
    if r:
        sprite.move((step,0))
    #redraw the screen
    display.fill(pygame.Color('white'))
    #display = display.convert_alpha()
    #area = pygame.Rect(x, 0, w, h)
    display.blit(sprite.scene(), (0,0))
    #display.blit(intermediate, (0,0))
    pygame.display.flip()
