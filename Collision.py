# Collision_In_2-Dimension
import time
import pygame
import random
from os import system
from math import inf as infinity
frameRate = 200
collisions = []
dt = 1/200
class obj:
    screen_size = [800, 800]
    def __init__(self, mass, pos, radius, color = (0, 0, 0), acceleration = 0, velx = 0, vely = 0, e = 1, number = None):
        self.mass = mass
        self.pos = pygame.Vector2(pos[0],pos[1])
        self.radius = radius
        self.color = color
        self.x = velx
        self.y = vely
        self.vel = pygame.math.Vector2(self.x, self.y)
        self.a = acceleration
        self.e = e
        self.number = number
        self.stop = None
    
    def display(self):
        try:
            pygame.draw.circle(screen, self.color, (round(self.pos[0]),round(self.pos[1])), self.radius)
        except:
            print(self.color)
    
    def update(self, dt):
        if abs(self.x) > 10000:
            self.x = (abs(self.x)/(self.x))*1000
        if abs(self.y) > 10000:
            self.y = (abs(self.y)/(self.y))*1000
        if self.stop != True:
            self.pos += self.vel*dt

            # self.y += 980 *dt
            if self.pos[0] > obj.screen_size[0]-self.radius:
                self.pos[0] -= 2*(self.pos[0]-self.screen_size[0]+self.radius)
                self.x *= -1
            elif self.pos[0] < self.radius:
                self.pos[0] += 2*(self.radius-self.pos[0])
                self.x *= -1

            if self.pos[1] > obj.screen_size[1]-self.radius:
                self.pos[1] -= 2*(self.pos[1]-self.screen_size[1]+self.radius)
                self.y *= -1
            elif self.pos[1] < self.radius:
                self.pos[1] += 2*(self.radius-self.pos[1])
                self.y *= -1
            self.vel = pygame.Vector2(self.x,self.y)
            if self.stop == False:
                self.stop = None
        else:
            self.stop = False
            

    def friction(self, gravity, mu):
        pass
    
    def collision(self, group:list, collisions:list, dt):
        for i in group:
            if [self.number, i.number] not in collisions:
                if (i.pos[0] - self.pos[0]) <= i.radius + self.radius:
                    if (i.pos[1] - self.pos[1]) <= i.radius + self.radius:
                        if distance(i.pos, self.pos) <= i.radius + self.radius:
                            
                            self.vel, i.vel = self.vel - (2*i.mass/(self.mass+i.mass)) * pygame.math.Vector2.project((self.vel - i.vel), (self.pos - i.pos)), i.vel - (2*self.mass/(self.mass+i.mass)) * pygame.math.Vector2.project((i.vel - self.vel), (i.pos - self.pos))
                            
                            self.x = self.vel[0]
                            self.y = self.vel[1]
                            i.x = i.vel[0]
                            i.y = i.vel[1]


                            self.color = [abs(self.color[0]+ (0.5-random.random())*20)%256, abs(self.color[1]+ (0.5-random.random())*20)%256, abs(self.color[2]+ (0.5-random.random())*20)%256]
                            i.color = [abs(i.color[0]+ (0.5-random.random())*20)%256, abs(i.color[1]+ (0.5-random.random())*20)%256, abs(i.color[2]+ (0.5-random.random())*20)%256]

                            self.update(dt *2)
                            i.update(dt *2)

                            if self.stop == None:
                                self.stop = True
                            if i.stop == None:
                                i.stop = True

                            dist = distance(i.pos, self.pos)
                            if dist < i.radius + self.radius:
                                if i.pos[0]-self.pos[0] == 0:
                                    i.pos[1] += sign(i.pos[1] - self.pos[1]) * abs(i.radius+self.radius-dist)/2
                                    self.pos[1] += sign(self.pos[1] - i.pos[1]) * abs(i.radius+self.radius-dist)/2
                                elif i.pos[1]-self.pos[1] == 0:
                                    i.pos[0] += sign(i.pos[0] - self.pos[0]) * abs(i.radius+self.radius-dist)/2
                                    self.pos[0] += sign(self.pos[0] - i.pos[0]) * abs(i.radius+self.radius-dist)/2
                                else:
                                    incHyp = (i.radius+self.radius-dist)
                                    incx = (incHyp/dist)*(abs(i.pos[0] - self.pos[0]))
                                    incy = (incHyp/dist)*(abs(i.pos[1] - self.pos[1]))
                                    i.pos[0] += incx* sign(i.pos[0] - self.pos[0])*((i.mass*i.radius)/(self.mass*self.radius+ i.mass*i.radius))
                                    i.pos[1] += incy *sign(i.pos[1] - self.pos[1])*((i.mass*i.radius)/(self.mass*self.radius+ i.mass*i.radius))
                                    self.pos[0] += incx* sign(self.pos[0] - i.pos[0])*((self.mass*self.radius)/(self.mass*self.radius+ i.mass*i.radius))
                                    self.pos[1] += incy *sign(self.pos[1] - i.pos[1])*((self.mass*self.radius)/(self.mass*self.radius+ i.mass*i.radius))
                                    print(f"Resolved Another bug!!! {[i.number, self.number]}")
                            return [[self.number, i.number], [i.number, self.number]]
        return []

def sign(num):
    return 1 if num > 0 else -1
                

def distance(point1,point2):
    return (((point1[0]-point2[0])**2) + ((point1[1]-point2[1])**2))**0.5


if __name__ == '__main__':
    balls = []
    for i in range(10):
        balls.append(obj(10+int(random.random()*30), (40 + int(random.random()*600),40 + int(random.random()*600)), 20, (int(random.random()*200)+56,int(random.random()*200)+56,int(random.random()*200)+56), 0, int((0.5-random.random())*500), int((0.5-random.random())*500), 1, i))
    
    pygame.init()
    screen = pygame.display.set_mode((800,800))
    pygame.display.set_caption("Collision")
    running = True
    initTime = time.time()
    clock = pygame.time.Clock()
    while running == True:
        collisions.clear()
        clock.tick(frameRate)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        #code
        screen.fill((150,150,150))
        for i in balls:
            collisions.extend(i.collision([objs for objs in balls if objs.number != i.number], collisions, dt))
            i.update(dt)
            i.display()
        pygame.display.update()
        endTime = time.time()
        dt = endTime-initTime
        initTime = endTime
        if dt != 0: frameRate = 1/dt
        else: frameRate = 1000
