import pygame, sys
from player import Player
from alienone import AlienOne
from alientwo import AlienTwo
from alienthree import AlienThree

pygame.display.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800,800))
background = pygame.image.load('hello.jpg').convert()
screen.blit(background,(0,0))
player = pygame.image.load('Juice Productions Logo copy.png').convert()
player = Player('player',"Juice Productions Logo copy.png",[80,80],[400,720],'keys')
alien = AlienOne('alien',"apple.png",[80,80])
alien2 = AlienTwo('alien',"apple.png",[80,80])
alien3 = AlienThree('alien',"apple.png",[80,80])
score = 0
running = True
while running:
    frametime = clock.tick(60)
    mousePOS = pygame.mouse.get_pos()
    screen.blit(background,(0,0))
    player.draw(screen)
    player.move(screen,frametime)
    alien.draw(screen)
    alien.move(screen,frametime)
    score = alien.detect_collision(player,score)
    alien2.draw(screen)
    alien2.move(screen,frametime)
    score = alien2.detect_collision(player,score)
    alien3.draw(screen)
    alien3.move(screen,frametime)
    score = alien3.detect_collision(player,score)
    pygame.display.update()
    #print(score)
    
    if(score < 0):
        running= False
    for event in pygame.event.get():
        
        if pygame.event.event_name(event.type) == 'Quit':
            running = False
    

    



pygame.display.quit()
print('-----------------------------------------------------------')
print('|                       GAME OVER                         |')
print('-----------------------------------------------------------')
print(f'|         You finised with a score of {score+1000000}!!                 |')
print('-----------------------------------------------------------')