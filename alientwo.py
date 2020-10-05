import pygame, entity, sys, random, math
class AlienTwo(entity.Entity):
    def __init__(self,name,image,dimensions):
        entity.Entity.__init__(self,name,image,dimensions)
        self.position = [random.randint(self.offset_X, 800-self.offset_X),random.randint(-200,self.offset_Y)]

    def move(self,screen,fps):
        self.position[1] += 0.12 * fps
        variable = 1/10*math.cos(0.03*self.position[1])
        self.position[0] += variable*fps
        #print(variable)
        
        self.draw(screen)
        
    def detect_collision(self,object,counter):
        if(round(self.position[0])+self.offset_X in range(object.position[0],object.position[0]+object.dimensions[0]) and round(self.position[1],0)+self.offset_Y in range(object.position[1],object.position[1]+object.dimensions[1])):
            counter+=1
            self.position = [random.randint(self.offset_X, 800-self.offset_X),random.randint(-200,self.offset_Y)]
            return counter
        if(self.position[1]>800):
            self.position = [random.randint(self.offset_X, 800-self.offset_X),random.randint(-200,self.offset_Y)]
            counter-=1000000
        return counter


    def draw(self,screen):
        screen.blit(self.image,self.position)