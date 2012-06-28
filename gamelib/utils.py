import pygame

def ColoredSurface((width,height),color):
    return (lambda surface: (surface, surface.fill(color))[0] )(pygame.Surface((width,height)))