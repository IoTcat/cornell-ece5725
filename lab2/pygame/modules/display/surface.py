class Surface:
    surface = None

    def __init__(self, surface):
        self.surface = surface
    


    def __lshift__(self, other):
        self.surface.blit(other.surface, other.rect)



