import pygame
from os import system
from math import atan2,degrees
class vector:
    def __init__(self, x : float, y : float):
        self.x = x
        self.y = y
    def angle(self):
        if self.x > 0 and self.y > 0:
            return degrees( atan2( abs(self.y), abs(self.x)))
        elif self.x < 0 and self.y > 0:
            return (90 + degrees( atan2( abs(self.y), abs(self.x))))
        elif self.x < 0 and self.y < 0:
            return (180 + degrees( atan2( abs(self.y), abs(self.x))))
        elif self.x > 0 and self.y < 0:
            return (270 + degrees( atan2( abs(self.y), abs(self.x))))
    def bouncex(self):
        self.x = -self.x
    def bouncey(self):
        self.y = -self.y

class coin:
    def __init__(self, surface, mass : float, pos : list, type : str):
        self.surface = surface
        self.mass = mass
        self.pos = pos
        self.type = type
        self.radius = (surface.get_width())/2
    def G(self):
        return [self.pos[0] + self.radius, self.pos[1] + self.radius]

def angle(x : float, y : float):
    if x > 0 and y > 0:
        return degrees( atan2( abs(y), abs(x)))
    elif x < 0 and y > 0:
        return (90 + degrees( atan2( abs(y), abs(x))))
    elif x < 0 and y < 0:
        return (180 + degrees( atan2( abs(y), abs(x))))
    elif x > 0 and y < 0:
        return (270 + degrees( atan2( abs(y), abs(x))))
FoNt = 0
FoNtprint = 0
COINS = [
    [],
    [coin( pygame.transform.scale(pygame.image.load('Images/Blue Ball.png'),[30,30]), 15, [400,400], 'Blue'), vector(5,6)],
    [coin( pygame.transform.scale(pygame.image.load('Images/Red Ball.png'),[30,30]), 15, [500,500], 'Red'), vector(6,7)]

]
def cls():
    system("cls")
def font(a:str,b=18):
    global FoNt
    FoNt = pygame.font.SysFont(a,b)
def printpy(x:str,a=(100,400),y=(128,128,128)):
    global FoNt,FoNtprint
    FoNtprint = FoNt.render(x,True,y)
    screen.blit(FoNtprint,a)
def placement():
    global COINS
    for element in COINS[1:]:
        screen.blit(element[0].surface, element[0].pos)
        if (element[0].pos[0]) > 740:
            element[1].bouncex()
            element[0].pos[0] = 739
        elif  (element[0].pos[0]) < 30:
            element[1].bouncex()
            element[0].pos[0] = 31
            
        if (element[0].pos[1]) > 740:
            element[1].bouncey()
            element[0].pos[1] = 739
        elif (element[0].pos[1]) < 30:
            element[1].bouncey()
            element[0].pos[1] = 31
        element[0].pos[0] = element[0].pos[0] + round( element[1].x )
        element[0].pos[1] = element[0].pos[1] + round( element[1].y )

pygame.init()
screen = pygame.display.set_mode((800,800))
icon = pygame.image.load('Images/Icon.jpg')
pygame.display.set_caption("")
pygame.display.set_icon(icon)
cls()
running = True
clock = pygame.time.Clock()
while running == True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #Code Here
    screen.fill((100,100,100))
    placement()
    pygame.display.update()