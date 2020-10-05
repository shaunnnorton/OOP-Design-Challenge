import pygame, sys
from player import Player


pygame.display.init()
screen = pygame.display.set_mode((800,800))
background = pygame.image.load('hello.jpg').convert()
screen.blit(background,(0,0))
#py.draw.rect((30,30))

player = pygame.image.load('Juice Productions Logo copy.png').convert()

running = True
shaun = Player('shaun',"Juice Productions Logo copy.png",[30,30],[400,400],'mouse')

while running:
    mousePOS = pygame.mouse.get_pos()
    screen.blit(background,(0,0))
    shaun.draw(screen)
    shaun.move(screen)
    pygame.display.update()
    for event in pygame.event.get():
        if pygame.event.event_name(event.type) == 'Quit':
            running = False
    

    
print('---------------')
print(shaun.name)
pygame.display.quit()
