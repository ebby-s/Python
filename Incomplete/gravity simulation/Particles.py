import pygame, sys, time, math, random
from pygame.locals import *
pygame.init()
#pygame.key.set_repeat(10,10)
global G
global resolution
G = 0.001
resolution = (1600,900)
main_font = pygame.font.SysFont('Courier',18,True)

class Particle:

    def __init__(self,mass=100):
        """A massive object"""
        self.mass = mass
        self.density = 2
        self.pos = [800,450]
        self.velocity = [0,0]
        self.force = [0,0]
        self.color = (150,150,140)
        self.radius = int((self.mass**(1/3))/self.density)

    def draw(self,screen):    # Draw particle on screen
        pygame.draw.circle(screen,self.color,(int(self.x),int(self.y)),self.radius)

    def update(self):    # Update characteristics of particle
        self.radius = int((self.mass**(1/3))/self.density)
        self.velocity[0] += self.force[0]/self.mass
        self.velocity[1] += self.force[1]/self.mass
        self.pos[0] += self.velocity[0]
        self.pos[1] += self.velocity[1]
        if self.mass < 1000:
            self.color = (150,150,140)
            self.density = 5
        elif 1000 <= self.mass < 5000:
            self.color = (73,255,237)
            self.density = 1
        elif mass > 5000:
            self.color = (10,10,10)
            self.density = 100
        

    def attract(self,other):    # Calculate forces due to gravity from other particles
        if self != other:
            dx = other.pos[0] - self.pos[0]
            dy = other.pos[1] - self.pos[1]
            r = (dy**2+dx**2)**0.5
            magnitude = G*(self.mass*other.mass)/r**2
            xmagnitude = (dx/r)*magnitude
            ymagnitude = (dy/r)*magnitude
            self.velocity[0] += xmagnitude/self.mass
            self.velocity[1] += ymagnitude/self.mass
            other.velocity[0] -= xmagnitude/other.mass
            other.velocity[1] -= ymagnitude/other.mass

    def collide(self,other):    # Check if there is a collision
        r1 = self.radius
        r2 = other.radius
        r_total = r1 + r2
        dx = other.x - self.x
        dy = other.y - self.y
        if dx**2 + dy**2 > r_total**2:
            return False
        else:
            return True

