import pygame, entity, sys, random
class AlienOne(entity.Entity):
    def __init__(self,name,image,dimensions):
        entity.Entity.__init__(self,name,image,dimensions)
        self.position = [random.randint(self.offset_X, 800-self.offset_X),800+self.offset_Y]