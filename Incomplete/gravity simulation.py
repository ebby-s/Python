# A game about gravity
import pygame, sys, time, math, random
from pygame.locals import *
pygame.init()
fpsClock=pygame.time.Clock()
#pygame.key.set_repeat(10,10)
global G
G = 0.0001

class particle:

    def __init__(self,mass=100):
        """A massive object"""
        self.mass = mass
        self.x = 800
        self.y = 450
        self.xvelocity = 0
        self.yvelocity = 0
        self.xforce = 0
        self.yforce = 0
        self.color = (255,0,36)
        self.radius = int(self.mass**(1/3))

    def draw(self,screen):    # Draw particle on screen
        pygame.draw.circle(screen,self.color,(int(self.x),int(self.y)),self.radius)

    def update(self):    # Update velocity and position of particle
        self.xvelocity += self.xforce/self.mass
        self.yvelocity += self.yforce/self.mass
        self.x += self.xvelocity
        self.y += self.yvelocity

    def attract(self,particles):    # Calculate forces due to gravity from other particles
        for other in particles:
            if self != other:
                dx = other.x - self.x
                dy = other.y - self.y
                r = (dy**2+dx**2)**0.5
                magnitude = G*(self.mass*other.mass)/r**2
                xmagnitude = (dx/r)*magnitude
                ymagnitude = (dy/r)*magnitude
                self.xvelocity += xmagnitude
                self.yvelocity += ymagnitude
                other.xvelocity -= xmagnitude
                other.yvelocity -= ymagnitude

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

def border(particles):        # Bounce partieles off border at 80% initial velocity
    for particle in particles:
        r = particle.radius
        if particle.x <= r:
            particle.xvelocity = abs(particle.xvelocity)*0.8
        if particle.y <= r:
            particle.yvelocity = abs(particle.yvelocity)*0.8
        if particle.x >= 1600 - r:
            particle.xvelocity = -abs(particle.xvelocity)*0.8
        if particle.y >= 900 - r:
            particle.yvelocity = -abs(particle.yvelocity)*0.8

screen=pygame.display.set_mode((1600,900),0,32)
pygame.display.set_caption('FunForce')

particles  = [particle() for i in range(5)]
for particle in particles:
    particle.x = random.randint(100,1500)
    particle.y = random.randint(100,800)
particles[0].color = (0,36,255)
particles[1].color = (36,255,0)

while True:
    screen.fill((0,0,0))
    
    for particle in particles:
        particle.update()
        particle.draw(screen)

    border(particles)

    for particle in particles:
        particle.attract(particles)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            if (event.key == K_LEFT):
                particles[0].xforce = -5
            elif (event.key == K_RIGHT):
                particles[0].xforce = 5
            elif (event.key == K_UP):
                particles[0].yforce = -5
            elif (event.key == K_DOWN):
                particles[0].yforce = 5
            elif (event.key == K_a):
                particles[1].xforce = -5
            elif (event.key == K_d):
                particles[1].xforce = 5
            elif (event.key == K_w):
                particles[1].yforce = -5
            elif (event.key == K_s):
                particles[1].yforce = 5
        else:
            particles[0].xforce = 0
            particles[0].yforce = 0
            particles[1].xforce = 0
            particles[1].yforce = 0

    pygame.display.update()
    fpsClock.tick(120)
