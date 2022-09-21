

import pygame
import numpy as np
from entity import Entity

class Text(Entity):
    text = ''
    color = 255,255,255
    size = 35
    def __init__(self, text = 'default', color = (255,255,255), position = [200, 200], size = 35, speed = [0,0]):
        self.speed = np.array(speed)
        self.text = text
        self.color = color
        self.size = size
        self.refresh()


    def refresh(self):
        self.surface = pygame.font.SysFont('Corbel',self.size, True).render(self.text, True, self.color)
        self.rect = self.surface.get_rect()
