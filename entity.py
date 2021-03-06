#Imports
import pygame
from abc import ABC,abstractmethod
#------------------------------------------------------------------------------------------------------------------------------------
class Entity(ABC):
    '''Abstract class that all Entities will enheriet from'''  
    def __init__(self,name,image,dimensions):
        """Intialize the class with name(string), image(string), 
        and dimensions(list). Calculate offsets for x and y dimensions"""
        self.name = name
        self._image = pygame.image.load(image).convert_alpha()
        self._dimensions = dimensions
        self._offset_X = dimensions[0]//2
        self._offset_Y = dimensions[1]//2
#------------------------------------------------------------------------------------------------------------------------------------
    @abstractmethod
    def move(self):
        """Should define how the Entity will move"""
        pass
#------------------------------------------------------------------------------------------------------------------------------------
    @abstractmethod
    def draw(self):
        pass