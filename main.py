import pygame, sys
from level import Level
score = 0
pygame.display.init()
screen = pygame.display.set_mode((800,800))

Level1=Level(1,10,'shaun','3-Norton-BuffManFaceAni.png',[64,64],[400,720],'keys','shaun',[64,64],'Deshawndre enemy walk copy.png',0.12,4,'DesignChallengeBG.png',screen)
Level2=Level(2,10,'shaun','3-Norton-BuffManFaceAni.png',[64,64],[400,720],'keys','shaun',[64,64],'Deshawndre enemy walk copy.png',0.12,2,'DesignChallengeBG.png',screen)
Level3=Level(3,5,'shaun','3-Norton-BuffManFaceAni.png',[64,64],[400,720],'keys','shaun',[64,64],'Deshawndre enemy walk copy.png',0.12,6,'DesignChallengeBG.png',screen)
Level1.start_level()

if(Level1.score>1):
    
    score += Level1.score
    Level2.start_level()
if(Level2.score>1):
    score += Level2.score
    Level3.start_level()
score+=Level3.score

    
#------------------------------------------------------------------------------------------------------------------------------------


    


#------------------------------------------------------------------------------------------------------------------------------------

pygame.display.quit()
print(score)
