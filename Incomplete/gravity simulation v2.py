import pygame, sys, time, math, random
from pygame.locals import *
pygame.init()
fpsClock=pygame.time.Clock()
global G
global resolution
G = 0.001
resolution = (1600,900)
main_font = pygame.font.SysFont('Courier',18,True)

class Particle:
    
    def __init__(self,contents=[100,0],density=1):
        """A massive object"""
        self.contents = contents
        self.mass = sum(self.contents)
        self.density = 2
        self.pos = [800,450]
        self.velocity = [0,0]
        self.force = [0,0]
        self.color = (150,150,140)
        self.radius = int((self.mass**(1/3))/self.density)

    def draw(self,screen):    # Draw particle on screen
        pygame.draw.circle(screen,self.color,(int(self.pos[0]),int(self.pos[1])),self.radius)

    def update(self):    # Update characteristics of particle
        self.radius = int((self.mass**(1/3))/self.density)
        self.velocity[0] += self.force[0]/self.mass
        self.velocity[1] += self.force[1]/self.mass
        self.pos[0] += self.velocity[0]
        self.pos[1] += self.velocity[1]
        self.mass = sum(self.contents)
        self.density = (1*self.contents[0]+0.2*self.contents[1])/self.mass
        '''
        if self.mass < 1000:
            self.color = (150,150,140)
            self.density = 1
        elif 1000 <= self.mass < 5000:
            self.color = (73,255,237)
            self.density = 0.5
        elif self.mass > 5000:
            self.color = (20,20,20)
            self.density = 5
        '''

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
            particle.velocity[0] = abs(particle.velocity[0])*0.8
        if particle.pos[1] <= r:
            particle.velocity[1] = abs(particle.velocity[1])*0.8
        if particle.pos[0] >= resolution[0] - r:
            particle.velocity[0] = -abs(particle.velocity[0])*0.8
        if particle.pos[1] >= resolution[1] - r:
            particle.velocity[1] = -abs(particle.velocity[1])*0.8

def collision_detect(particles):
    for i,particle in enumerate(particles):
        for other in particles[i+1:]:
            if particle.collide(other):
                xmomentum = particle.mass*particle.velocity[0] + other.mass*other.velocity[0]
                ymomentum = particle.mass*particle.velocity[1] + other.mass*other.velocity[1]
                mass = particle.mass + other.mass
                contents = [particle.contents[0]+other.contents[0],particle.contents[1]+other.contents[1]]
                if particle.mass >= other.mass:
                    particle.contents = contents
                    particle.velocity[0] = xmomentum/mass
                    particle.velocity[1] = ymomentum/mass
                    if particles.index(other) in [0,1]:
                        particles.insert(particles.index(other)+1,Particle())
                        particles[particles.index(other)+1].pos[0] = random.randint(resolution[0]*0.1,resolution[0]*0.9)
                        particles[particles.index(other)+1].pos[1] = random.randint(resolution[1]*0.1,resolution[1]*0.9)
                    del(particles[particles.index(other)])
                else:
                    other.contents = contents
                    other.xvelocity = xmomentum/mass
                    other.yvelocity = ymomentum/mass
                    if particles.index(particle) in [0,1]:
                        particles.insert(particles.index(particle)+1,Particle())
                        particles[particles.index(particle)+1].pos[0] = random.randint(resolution[0]*0.1,resolution[0]*0.9)
                        particles[particles.index(particle)+1].pos[1] = random.randint(resolution[1]*0.1,resolution[1]*0.9)
                    del(particles[particles.index(particle)])

screen=pygame.display.set_mode(resolution,0,32)

particles  = [Particle() for i in range(2)]
for particle in particles:
    particle.pos[0] = random.randint(resolution[0]*0.1,resolution[0]*0.9)
    particle.pos[1] = random.randint(resolution[1]*0.1,resolution[1]*0.9)
particles[0].color = (0,36,255)
particles[1].color = (36,255,0)

while True:
    screen.fill((0,0,0))

    while len(particles) < 30:
        particles.append(Particle([random.randint(10,50),random.randint(1,5)]))
        particles[-1].pos[0] = random.randint(resolution[0]*0.1,resolution[0]*0.9)
        particles[-1].pos[1] = random.randint(resolution[1]*0.1,resolution[1]*0.9)
    
    particles[0].color = (0,36,255)
    particles[1].color = (36,255,0)

    for particle in particles:
        particle.update()
        particle.draw(screen)

    border(particles)
    
    collision_detect(particles)

    for i,particle in enumerate(particles):
        for other in particles[i+1:]:
            particle.attract(other)

    for i,text in enumerate(["Player 1 mass: "+str(particles[0].contents),"Player 2 mass: "+str(particles[1].contents)]):
        screen.blit(main_font.render(text,True,(255,255,255)),(10,10+30*i))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            if (event.key == K_LEFT):
                particles[0].force[0] = -5
            elif (event.key == K_RIGHT):
                particles[0].force[0] = 5
            elif (event.key == K_UP):
                particles[0].force[1] = -5
            elif (event.key == K_DOWN):
                particles[0].force[1] = 5
            if (event.key == K_a):
                particles[1].force[0] = -5
            elif (event.key == K_d):
                particles[1].force[0] = 5
            elif (event.key == K_w):
                particles[1].force[1] = -5
            elif (event.key == K_s):
                particles[1].force[1] = 5
        else:
            particles[0].force[0] = 0
            particles[0].force[1] = 0
            particles[1].force[0] = 0
            particles[1].force[1] = 0

    pygame.display.update()
    fpsClock.tick(120)
