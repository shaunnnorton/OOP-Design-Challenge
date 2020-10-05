import pygame, entity, sys, random, math
class AlienThree(entity.Entity):
    def __init__(self,name,image,dimensions):
        entity.Entity.__init__(self,name,image,dimensions)
        self.position = [random.randint(self.offset_X, 800-self.offset_X),random.randint(-200,self.offset_Y)]

    def move(self,screen,fps):
        directions = ['up','left','right','down','down','down','down','down','down','down','down','down']
        variable = random.choice(directions)
        if(variable == 'up'):
            self.position[1] += -0.12*fps
        if(variable == 'left'):
            self.position[0] += -0.12*fps
        if(variable == 'right'):
            self.position[0] += 0.12*fps
        if(variable == 'down'):
            self.position[1] += 0.12*fps
        
        #print(variable)
        if(self.position[1]>800):
            self.position = [random.randint(self.offset_X, 800-self.offset_X),random.randint(-200,self.offset_Y)]
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