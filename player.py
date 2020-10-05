import pygame, entity, sys

class Player(entity.Entity):
    def __init__(self,name,image,dimensions,startingPos,inputType):
        entity.Entity.__init__(self,name,image,dimensions)
        self.position = startingPos
        self.inputType = inputType
        
    def move(self,screen,fps):
        if(self.inputType == 'mouse' and fps > 15):
            mousePos = pygame.mouse.get_pos()
            self.position[0] = mousePos[0] - self.offset_X
            self.draw(screen)
            #pygame.display.update()
            return

        if(self.inputType == 'keys'):
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
                
                
                

    def draw(self,screen):
        screen.blit(self.image,self.position)

    
   

        

        

