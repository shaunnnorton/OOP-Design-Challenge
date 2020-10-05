import pygame, sys
from player import Player
from alienone import AlienOne
from alientwo import AlienTwo
from alienthree import AlienThree
#------------------------------------------------------------------------------------------------------------------------------------
#Initialize Screen, Clock, Background, and score.
pygame.display.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800,800))
background = pygame.image.load('DesignChallengeBG.png').convert()
screen.blit(background,(0,0))
score = 0
#------------------------------------------------------------------------------------------------------------------------------------
#Intialize Player and Three Alien Types.
player = Player('player',"3-Norton-BuffManFaceAni.png",[64,64],[400,720],'keys')
alien = AlienOne('alien',"Deshawndre enemy walk copy.png",[64,64])
alien2 = AlienTwo('alien',"Deshawndre enemy walk copy.png",[64,64])
alien3 = AlienThree('alien',"Deshawndre enemy walk copy.png",[64,64])
#------------------------------------------------------------------------------------------------------------------------------------
#Run the game
running = True
while running:
    frametime = clock.tick(60) #FPS = 60
    screen.blit(background,(0,0)) #Draw background Each frame.
    player.draw(screen) #Draw Player
    player.move(screen,frametime) #Changes position
    alien.draw(screen) #Draw Alienone at current position
    alien.move(screen,frametime)#Changes position
    score = alien.detect_collision(player,score) #Check if alien is colliding with player
    alien2.draw(screen)#Draw Alien2 at current position
    alien2.move(screen,frametime)#Changes position
    score = alien2.detect_collision(player,score) #Check if alien is colliding with player
    alien3.draw(screen)#Draw Aline 3 
    alien3.move(screen,frametime)#Changes position
    score = alien3.detect_collision(player,score) #Check if alien is colliding with player
    pygame.display.update() #Show the new Frame
    
    #------------------------------------------------------------------------------------------------------------------------------------
    #Ends the game if a alien gets to the bottom or if the window is closed.
    if(score < 0):
        running= False
    for event in pygame.event.get():
        
        if pygame.event.event_name(event.type) == 'Quit':
            score -= 1000000
            running = False
    

    


#------------------------------------------------------------------------------------------------------------------------------------

pygame.display.quit()
print('-----------------------------------------------------------')
print('|                       GAME OVER                         |')
print('-----------------------------------------------------------')
print(f'|         You finised with a score of {score+1000000}!!                 |')
print('-----------------------------------------------------------')