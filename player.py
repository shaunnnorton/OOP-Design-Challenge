#Imports
import pygame, entity, sys
#------------------------------------------------------------------------------------------------------------------------------------
class Player(entity.Entity):
    """Class for a entity that the player controls and is the catching mechinism"""
    def __init__(self,name,image,dimensions,startingPos,inputType):
        """Intializes class with name(string),image(string),
        dimensions(list),startingPos(list),inputType('mouse' or 'keys')"""
        entity.Entity.__init__(self,name,image,dimensions)
        self.position = startingPos
        self.__inputType = inputType
#------------------------------------------------------------------------------------------------------------------------------------
    def move(self,screen,fps):
        """Defines how to move the player. Takes a screen object
         and an output from clock.tick(). Allows the player character
          to be moved left and right with user input."""
        if(self.__inputType == 'mouse' and fps > 15):
            mousePos = pygame.mouse.get_pos()
            self.position[0] = mousePos[0] - self.offset_X
            self.draw(screen)
            #pygame.display.update()
            return
        if(self.__inputType == 'keys'):
            if(1 in pygame.key.get_pressed()):
                for key in pygame.key.get_pressed():
                    if(key == 1):
                        if(pygame.key.get_pressed().index(key)==79):
                            self.position[0] += 1*fps
                            #print("right")
                        if(pygame.key.get_pressed().index(key)==80):
                            self.position[0] -= 1*fps
                            #print("left")
                        if(self.position[0]<-1):
                            self.position[0] = 5
                        if(self.position[0]>800-self.offset_X):
                            self.position[0] = 800-self.offset_X

                        self.draw(screen)
                        #pygame.display.update()
                        return
                
#------------------------------------------------------------------------------------------------------------------------------------

    def draw(self,screen):
        """Draws image in a new position on the screen 
        object provided.(Screen needs to be updated to appear)"""
        screen.blit(self.image,self.position)

    
   

        

        

