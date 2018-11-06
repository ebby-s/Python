import pygame, random
from pygame.locals import *
pygame.init()
global G
global resolution
G = 1
resolution = (1600,900)

class Particle:
    
    def __init__(self,mass):
        self.mass = mass
        self.pos = [800,450]
        self.velocity = [0,0]
        self.force = [0,0]
        self.color = (255,255,255)
        self.radius = round(2*self.mass**(1/3))

    def draw(self,screen):    # Draw particle on screen
        pygame.draw.circle(screen,self.color,(int(self.pos[0]),int(self.pos[1])),self.radius)

    def update(self):    # Update characteristics of particle
        self.radius = round(2*self.mass**(1/3))
        self.velocity[0] += self.force[0]/self.mass
        self.velocity[1] += self.force[1]/self.mass
        self.pos[0] += self.velocity[0]
        self.pos[1] += self.velocity[1]

    def attract(self,other):    # Calculate forces due to gravity from other particles
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
        dx = other.pos[0] - self.pos[0]
        dy = other.pos[1] - self.pos[1]
        if dx**2 + dy**2 > r_total**2:
            return False
        else:
            return True

def border(particles):        # Bounce partieles off border at 80% initial velocity
    for particle in particles:
        r = particle.radius
        if particle.pos[0] <= r:
            particle.velocity[0] = abs(particle.velocity[0])
        if particle.pos[1] <= r:
            particle.velocity[1] = abs(particle.velocity[1])
        if particle.pos[0] >= resolution[0] - r:
            particle.velocity[0] = -abs(particle.velocity[0])
        if particle.pos[1] >= resolution[1] - r:
            particle.velocity[1] = -abs(particle.velocity[1])

def collision_detect(particles):
    for i,particle in enumerate(particles):
        for other in particles[i+1:]:
            if particle.collide(other):
                xmomentum = particle.mass*particle.velocity[0] + other.mass*other.velocity[0]
                ymomentum = particle.mass*particle.velocity[1] + other.mass*other.velocity[1]
                mass = particle.mass + other.mass
                if particle.mass >= other.mass:
                    particle.mass = mass
                    particle.velocity[0] = xmomentum/mass
                    particle.velocity[1] = ymomentum/mass
                    del(particles[particles.index(other)])
                else:
                    other.mass = mass
                    other.xvelocity = xmomentum/mass
                    other.yvelocity = ymomentum/mass
                    del(particles[particles.index(particle)])

def start():
    screen = pygame.display.set_mode(resolution,0,32)

    particles  = [Particle(1) for i in range(200)]
    for particle in particles:
        particle.pos[0] = random.randint(resolution[0]*0.01,resolution[0]*0.99)
        particle.pos[1] = random.randint(resolution[1]*0.01,resolution[1]*0.99)
    return [screen,particles]

[screen,particles] = start()

while True:
    screen.fill((0,0,0))

    border(particles)
    collision_detect(particles)

    for i,particle in enumerate(particles):
        particle.update()
        particle.draw(screen)
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

'''
while True:
    screen.fill((0,0,0))

    for particle in particles:
        particle.update()
        particle.draw(screen)

    border(particles)
    collision_detect(particles)

    for i,particle in enumerate(particles):
        for other in particles[i+1:]:
            particle.attract(other)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if   event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif event.key == K_r:
                [screen,particles] = start()

    pygame.display.update()
    fpsClock.tick(120)
'''
