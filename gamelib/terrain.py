import pygame

class Terrain:
    """
        This class is defined in order to allow an uneven floor.
        
        Attributes:
            map                         A terrain map, made up of (x,y) pairs.
                                        Format: map = [(x1,y1),(x2,y2),(x3,y3),...,(xn,yn)]
            
        Methods:
            groundtest                  A simple test to decide whether a certain (x,y) point lies at or below ground level.
                                        Test returns True if point is below ground level.
                                        function returns a 2-tuple with the resulting boolean and a new point (x,y'), 
                                        where x is the same as the input and y' is the ground height at the given x.
    """
    def __init__(self, tmap):
        self.map = tmap
        
       
    def groundtest(self, (x,y)):
        if x < self.map[0][0]: return None
        p1 = ()
        p2 = ()
        for point in self.map:
            if point[0] > x:
                p1 = point
                break
            p2 = point
        m = (p2[1]-p1[1])/(p2[0]-p1[0])
        yground = m*(x-p1[0]) + p1[1]
        return (    y<=yground,
                    (int(x), int(yground))    )