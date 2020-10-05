import pygame
from abc import ABC,abstractmethod
class Entity(ABC):
    def __init__(self,name,image,dimensions):
        self.name = name
        self.image = pygame.image.load(image).convert_alpha()
        self.dimensions = dimensions
        self.offset_X = dimensions[0]/2
        self.offset_Y = dimensions[1]/2

    @abstractmethod
    def move(self):
        pass

   
        