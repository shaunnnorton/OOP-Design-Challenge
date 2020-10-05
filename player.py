import pygame, entity, sys

class Player(entity.Entity):
    def __init__(self,name,image,dimensions,startingPos,inputType):
        entity.Entity.__init__(self,name,image,dimensions)
        self.position = startingPos
        self.inputType = inputType
        
    def move(self,screen):
        if(self.inputType == 'mouse'):
            mousePos = pygame.mouse.get_pos()
            self.position[0] = mousePos[0] - self.offset_X
            self.draw(screen)
            pygame.display.update()
            return

        if(self.inputType == 'keys'):
            if(1 in pygame.key.get_pressed()):
                for key in pygame.key.get_pressed():
                    if(key == 1):
                        if(pygame.key.get_pressed().index(key)==79):
                            self.position[0] += 3
                            print("right")
                        if(pygame.key.get_pressed().index(key)==80):
                            self.position[0] -= 3
                            print("left")


                        self.draw(screen)
                        pygame.display.update()
                        return
                
                
                """if(pygame.event.event_name(event.type) == 'KeyDown'):    
                    if(event.__dict__['key'] == 1073741904):
                        self.position[0] -= 6
                        print("ajl;fjaelghaowg")
                    if(event.__dict__['key'] == 1073741903):
                        self.position[0] += 6
                        print("ffffffffffg")"""


    def draw(self,screen):
        screen.blit(self.image,self.position)

    
   

        

        

