
import pygame
import numpy as np
from entity import Entity

class VButton(Entity):
    text = None
    color = 100,100,100
    def __init__(self, text = None, position = [200, 200], size = (100, 100), color = (100,100,100), speed = [0,0]):
        self.speed = np.array(speed)
        self.color = color
        self.text = text
        self.rect = pygame.Rect((position[0]-size[0]/2, position[1]-size[1]/2), size)
        self.refresh()


    def refresh(self):
        self.surface = pygame.Surface(self.rect.size)
        pygame.draw.rect(self.surface, self.color, self.surface.get_rect())
        if self.text != None:
            self.text.rect.centerx = self.rect.size[0] / 2
            self.text.rect.centery = self.rect.size[1] / 2
            self << self.text



