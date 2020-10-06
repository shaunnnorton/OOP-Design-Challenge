#Imports
import pygame, entity, sys, random
#------------------------------------------------------------------------------------------------------------------------------------
class AlienOne(entity.Entity):
    """Class to create and entity to be the first type of alien"""
    def __init__(self,name,image,dimensions,speed):
        """Initializes class with name(string),image(string),dimensions(list). 
        Sets the position of to a random position along the top and a random 
        position above the visual line"""
        entity.Entity.__init__(self,name,image,dimensions)
        self.__position = [random.randint(self.offset_X, 800-self.offset_X),random.randint(-200,self.offset_Y)]
        self.speed = speed
#------------------------------------------------------------------------------------------------------------------------------------
    def move(self,screen,fps):
        """Moves the current position down at speedpixles per frame"""
        self.__position[1] += self.speed * fps
        
        self.draw(screen)
#------------------------------------------------------------------------------------------------------------------------------------
    def detect_collision(self,object,counter):
        """Tests if the center of the object is anywhere inside the provided object then adds 
        one to the counter. Must have accurate dimensions in both objects. Ends the game if 
        an object hits the bottom of the screen"""
        if(self.__position[0]+self.offset_X in range(object.position[0],object.position[0]+object.dimensions[0]) and round(self.__position[1],0)+self.offset_Y in range(object.position[1],object.position[1]+object.dimensions[1])):
            counter+=1
            self.__position = [random.randint(self.offset_X, 800-self.offset_X),random.randint(-200,self.offset_Y)]
            return counter
        if(self.__position[1]>800):
            self.__position = [random.randint(self.offset_X, 800-self.offset_X),random.randint(-200,self.offset_Y)]
            counter-=1000000
        return counter

#------------------------------------------------------------------------------------------------------------------------------------
    def draw(self,screen):
        """Draws image in a new position on the screen 
        object provided.(Screen needs to be updated to appear)"""
        screen.blit(self.image,self.__position)