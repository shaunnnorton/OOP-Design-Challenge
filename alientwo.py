#Imports
import pygame, entity, sys, random, math
#------------------------------------------------------------------------------------------------------------------------------------
class AlienTwo(entity.Entity):
    """Class to create and entity to be the second type of alien"""
    def __init__(self,name,image,dimensions):
        """Initializes class with name(string),image(string),dimensions(list). 
        Sets the position of to a random position along the top and a random 
        position above the visual line"""
        entity.Entity.__init__(self,name,image,dimensions)
        self.__position = [random.randint(self.offset_X, 800-self.offset_X),random.randint(-200,self.offset_Y)]
#------------------------------------------------------------------------------------------------------------------------------------
    def move(self,screen,fps):
        """Moves the current position down and side to side at 0.12pixles per frame"""
        self.__position[1] += 0.12 * fps
        variable = 1/10*math.cos(0.03*self.__position[1])
        self.__position[0] += variable*fps
        self.draw(screen)
#------------------------------------------------------------------------------------------------------------------------------------
    def detect_collision(self,object,counter):
        """Tests if the center of the object is anywhere inside the provided object then adds 
        one to the counter. Must have accurate dimensions in both objects. Ends the game if 
        an object hits the bottom of the screen"""
        if(round(self.__position[0])+self.offset_X in range(object.position[0],object.position[0]+object.dimensions[0]) and round(self.__position[1],0)+self.offset_Y in range(object.position[1],object.position[1]+object.dimensions[1])):
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