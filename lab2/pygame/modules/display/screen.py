import pygame
from surface import Surface

class Screen(Surface):
    __background = (0,0,0)
    weith = 0
    height = 0
    def __init__(self, width, height, background = (0,0,0)):
        self.surface = pygame.display.set_mode((width, height))
        self.__background = background
        self.width = width
        self.height = height


    def constrain(self, entity):
        if entity.left() < 0:
            entity.speed[0] = -entity.speed[0]
            entity.move([-entity.left(),0])
        if entity.top() < 0:
            entity.speed[1] = -entity.speed[1]
            entity.move([0,-entity.top()])
        if entity.right() > self.width:
            entity.speed[0] = -entity.speed[0]
            entity.move([(-entity.right()+self.width),0])
        if entity.bottom() > self.height:
            entity.speed[1] = -entity.speed[1]
            entity.move([0,(-entity.bottom()+self.height)])

    def clear(self):
        self.surface.fill(self.__background)