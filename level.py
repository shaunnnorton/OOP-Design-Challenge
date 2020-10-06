import pygame, sys, random
from player import Player
from alienone import AlienOne
from alientwo import AlienTwo
from alienthree import AlienThree

class Level(Player,AlienOne,AlienTwo,AlienThree):
    def __init__(self,level_number,score_target,name,player_image,player_dimensions,player_startingPos,inputType,alien_names,alien_dimensions,alien_image,alien_speed,number_ofaliens, background_image, screen):
        self.level_number = level_number
        self.player = Player(name,player_image,player_dimensions,player_startingPos,inputType)
        self.alien_dimensions = alien_dimensions
        self.alien_names = alien_names
        self.alien_image = alien_image
        self.alien_speed = alien_speed
        self.number_of_aliens = number_ofaliens
        self.aliens = {}
        self.background = pygame.image.load(background_image).convert()
        self.score = 0
        self.screen = screen
        self.score_target = score_target
        for i in range(1,self.number_of_aliens+1):
            self.aliens[f'alien{i}'] = random.choice([AlienOne(self.alien_names,self.alien_image,self.alien_dimensions,self.alien_speed),AlienTwo(self.alien_names,self.alien_image,self.alien_dimensions,self.alien_speed),AlienThree(self.alien_names,self.alien_image,self.alien_dimensions,self.alien_speed)])


    def start_level(self):
        pygame.display.set_caption(f"Level {self.level_number}")
        clock = pygame.time.Clock()
        running = True
        while running:
            frametime = clock.tick(60) #FPS = 60
            self.screen.blit(self.background,(0,0)) #Draw background Each frame.
            self.player.draw(self.screen) #Draw Player
            self.player.move(self.screen,frametime) #Changes position
            for i in self.aliens:
                self.aliens[i].draw(self.screen)
                self.aliens[i].move(self.screen,frametime)
                self.score = self.aliens[i].detect_collision(self.player,self.score)
            pygame.display.update() #Show the new Frame
            
            #------------------------------------------------------------------------------------------------------------------------------------
            #Ends the game if a alien gets to the bottom or if the window is closed.
            if(self.score >= self.score_target):
                running = False
                self.end_level()
            if(self.score < 0):
                running= False
                self.end_level()
            for event in pygame.event.get():
                
                if pygame.event.event_name(event.type) == 'Quit':
                    self.score -= 1000000
                    running = False
                    self.end_level()

    def end_level(self):
        if(self.score > 0):
            print("Level Complete")
            return self.score
        else:
            print('-----------------------------------------------------------')
            print('|                       GAME OVER                         |')
            print('-----------------------------------------------------------')
            print(f'|         You finised with a score of {self.score+1000000}!!                 |')
            print('-----------------------------------------------------------')
            return self.score

