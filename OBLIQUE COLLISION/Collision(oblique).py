import pygame
from os import system
from math import atan2,degrees,radians,sin,cos
collisions = []     #This list stores all the collisions 
LOI = []    #Line Of Impact
class vector:
    def __init__(self, x : float, y : float):
        self.x = x
        self.y = y
    def angle(self):
        if self.x > 0 and self.y > 0:
            return degrees( atan2( abs(self.y), abs(self.x) ))
        elif self.x < 0 and self.y > 0:
            return (90 + degrees( atan2( abs(self.y), abs(self.x) )))
        elif self.x < 0 and self.y < 0:
            return (180 + degrees( atan2( abs(self.y), abs(self.x) )))
        elif self.x > 0 and self.y < 0:
            return (270 + degrees( atan2( abs(self.y), abs(self.x) )))
        else:
            if self.x == 0 and self.y!= 0:
                if self.y > 0:
                    return degrees( atan2( abs(self.y), abs(self.x) ))
                else:
                    return (180 + degrees( atan2( abs(self.y), abs(self.x) )))
            elif self.x != 0:
                if self.x > 0:
                    return degrees( atan2( abs(self.y), abs(self.x) ))
                else:
                    return (180 + degrees( atan2( abs(self.y), abs(self.x) )))
            else:
                return 0

    def resultant(self):
        return ((((self.x)**2)+((self.y)**2))**0.5)
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

def angle(y : float, x : float):
    if x > 0 and y > 0:
        return degrees( atan2( abs(y), abs(x) ))
    elif x < 0 and y > 0:
        return (90 + degrees( atan2( abs(y), abs(x) )))
    elif x < 0 and y < 0:
        return (180 + degrees( atan2( abs(y), abs(x) )))
    elif x > 0 and y < 0:
        return (270 + degrees( atan2( abs(y), abs(x) )))
    else:
        if x == 0 and y!= 0:
            if y > 0:
                return degrees( atan2( abs(y), abs(x) ))
            else:
                return (180 + degrees( atan2( abs(y), abs(x) )))
        elif x != 0:
            if x > 0:
                return degrees( atan2( abs(y), abs(x) ))
            else:
                return (180 + degrees( atan2( abs(y), abs(x) )))
        else:
            return 0
def resultant(x : float, y : float):
    return (((x**2)+(y**2))**0.5)
FoNt = 0
FoNtprint = 0
COINS = [
    [],
    [coin( pygame.transform.scale(pygame.image.load('Images/Blue Ball.png'),[50,50]), 50, [500,600], 'Blue'), vector(0,7), 1],
    [coin( pygame.transform.scale(pygame.image.load('Images/Red Ball.png'),[70,70]), 70, [435,300], 'Red'), vector(0,0), 2]

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
    global COINS,collisions, LOI
    for element in COINS[1:]:
        screen.blit(element[0].surface, element[0].pos)
        if (element[0].pos[0]) > (770-element[0].radius*2):
            element[1].bouncex()
            element[0].pos[0] = 769-element[0].radius*2
        elif  (element[0].pos[0]) < (30):
            element[1].bouncex()
            element[0].pos[0] = 31
            
        if (element[0].pos[1]) > (770-element[0].radius*2):
            element[1].bouncey()
            element[0].pos[1] = 769-element[0].radius*2
        elif (element[0].pos[1]) < (30):
            element[1].bouncey()
            element[0].pos[1] = 31
        element[0].pos[0] = element[0].pos[0] + round( element[1].x )
        element[0].pos[1] = element[0].pos[1] + round( element[1].y )
        collisions.clear()
        for element2 in COINS[1:]:
            if element[2] != element2[2]:
                if (([element2[2],element[2]] not in collisions) and ([element[2],element2[2]] not in collisions)):
                    if ((((element2[0].G()[0]-element[0].G()[0])**2) + ((element2[0].G()[1]-element[0].G()[1])**2))**0.5) < (element2[0].radius+element[0].radius):
                        LOI = [angle(( element2[0].G()[0] - element[0].G()[0] ), ( element2[0].G()[1] - element[0].G()[1] ))]   #theta
                        alpha = element[1].angle()
                        beta = element2[1].angle()
                        vels = [element[1].resultant()*(cos(radians(180-LOI[0]+alpha))), element2[1].resultant()*(cos(radians(LOI[0]-beta)))]
                        constant_vels = [element[1].resultant()*(sin(radians(180-LOI[0]+alpha))), element2[1].resultant()*(sin(radians(LOI[0]-beta)))]
                        vels[0], vels[1] = (1/(element[0].mass+element2[0].mass))*(vels[0]*(element[0].mass-element2[0].mass) + 2*vels[1]*element2[0].mass), (1/(element[0].mass+element2[0].mass))*(vels[1]*(element2[0].mass-element[0].mass) + 2*vels[0]*element[0].mass)
                        resultants = [resultant(vels[0],constant_vels[0]),resultant(vels[1],constant_vels[1])]
                        angles = [(angle(constant_vels[0],vels[0]) - LOI[0]), (angle(constant_vels[1],vels[1]) - LOI[0])]
                        element[1].x = resultants[0]*(cos(radians(angles[0])))
                        element[1].y = resultants[0]*(sin(radians(angles[0])))
                        element2[1].x = resultants[0]*(cos(radians(angles[1])))
                        element2[1].y = resultants[0]*(sin(radians(angles[1])))
                        collisions.append([element[2],element2[2]])
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
