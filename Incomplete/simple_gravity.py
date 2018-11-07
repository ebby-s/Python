import pygame, random, time, sys
from pygame.locals import *
pygame.init()
fpsClock=pygame.time.Clock()
global G
global resolution
G = 1
resolution = (1600,900)

# Good seeds, with initial particles and mass: [[3584879356604460687,8,25],[8741169891298822318,100,1],[183252150040625239,8,25]]

class Particle:
    
    def __init__(self,mass):
        self.mass = mass
        self.pos = [0,0]
        self.velocity = [0,0]
        self.radius = round(2*self.mass**(1/3))

    def draw(self,screen):    # Draw particle on screen
        pygame.draw.circle(screen,(255,255,255),(int(self.pos[0]),int(self.pos[1])),self.radius)

    def update(self):    # Update characteristics of particle
        self.pos[0] += self.velocity[0]
        self.pos[1] += self.velocity[1]

    def attract(self,other):    # Calculate forces due to gravity from other particles
        x = other.pos[0] - self.pos[0]
        y = other.pos[1] - self.pos[1]
        r = (y**2+x**2)**0.5
        magnitude = G*(self.mass*other.mass)/r**2
        xmagnitude = magnitude*(x/r)
        ymagnitude = magnitude*(y/r)
        self.velocity[0] += xmagnitude/self.mass
        self.velocity[1] += ymagnitude/self.mass
        other.velocity[0] -= xmagnitude/other.mass
        other.velocity[1] -= ymagnitude/other.mass

    def collide(self,other):    # Check if there is a collision
        r = self.radius + other.radius
        x = other.pos[0] - self.pos[0]
        y = other.pos[1] - self.pos[1]
        if x**2 + y**2 <= r**2:
            xmomentum = self.mass*self.velocity[0] + other.mass*other.velocity[0]
            ymomentum = self.mass*self.velocity[1] + other.mass*other.velocity[1]
            mass = self.mass + other.mass
            if self.mass >= other.mass:
                self.mass = mass
                self.velocity[0] = xmomentum/mass
                self.velocity[1] = ymomentum/mass
                self.radius = round(2*self.mass**(1/3))
                del(particles[particles.index(other)])
            else:
                other.mass = mass
                other.velocity[0] = xmomentum/mass
                other.velocity[1] = ymomentum/mass
                other.radius = round(2*other.mass**(1/3))
                del(particles[particles.index(self)])

def bounce_border(particle):        # Bounce partieles off border
    r = particle.radius
    if particle.pos[0] <= r:
        particle.velocity[0] = abs(particle.velocity[0])
    elif particle.pos[1] <= r:
        particle.velocity[1] = abs(particle.velocity[1])
    elif particle.pos[0] >= resolution[0] - r:
        particle.velocity[0] = -abs(particle.velocity[0])
    elif particle.pos[1] >= resolution[1] - r:
        particle.velocity[1] = -abs(particle.velocity[1])

def infinity_border(particle):        # Particles teleport to the other side of screen
    r = particle.radius
    if particle.pos[0] <= r:
        particle.pos[0] = resolution[0] - r - 1
    elif particle.pos[1] <= r:
        particle.pos[1] = resolution[1] - r - 1
    elif particle.pos[0] >= resolution[0] - r:
        particle.pos[0] = r + 1
    elif particle.pos[1] >= resolution[1] - r:
        particle.pos[1] = r + 1

def start(seed=random.randrange(sys.maxsize)):
    random.seed(seed)
    print("Seed was:", seed)
    screen = pygame.display.set_mode(resolution,0,32)

    particles  = [Particle(25) for i in range(8)]
    for particle in particles:
        particle.pos[0] = random.randint(resolution[0]*0.01,resolution[0]*0.99)
        particle.pos[1] = random.randint(resolution[1]*0.01,resolution[1]*0.99)
    return [screen,particles]

[screen,particles] = start()

while True:
    screen.fill((0,0,0))

    for i,particle in enumerate(particles):
        particle.update()
        particle.draw(screen)
        for other in particles[i+1:]:
            particle.collide(other)
        for other in particles[i+1:]:
            particle.attract(other)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        elif event.type == KEYDOWN:
            if   event.key == K_ESCAPE:
                pygame.quit()
                exit()
            elif event.key == K_r:
                [screen,particles] = start()
    
    pygame.display.update()
    #fpsClock.tick(90)


