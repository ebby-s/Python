import numpy as np
import matplotlib.pyplot as plt  
import pygame, random, time, sys
from pygame.locals import *
pygame.init()
pygame.display.set_caption("MolSim")
fpsClock=pygame.time.Clock()
global resolution
resolution = (700,700)
screen = pygame.display.set_mode(resolution,0,32)

class beads:
    
    def __init__(self, num_A):
        self.mult = 10
        self.kT = 0.1                            # value proportional to temperature?
        self.sigma_A = 1                            # van der waals radii
        self.sigma_B = 1
        self.sigma_AB = 1
        self.kspring = 1                         # spring constant for bond approximation
        self.epsilon_AA = 5 * self.kT                 # potential well depths
        self.epsilon_BB = 5 * self.kT
        self.epsilon_AB = self.kT
        self.rcutoffAA = 2.5 * self.sigma_A          # radius for simulating lennard jones potential
        self.rcutoffBB = 2.5 * self.sigma_B
        self.rcutoffAB = 2.5 * self.sigma_AB
        self.E_total = None                       # total energy of system
        num_B = 10 - num_A                     # ratio of A to B
        self.pos = []                       # store positions of beads of all beads in pos, A beads in posA and B beads in posB
        self.posA = []
        self.posB = []
        self.next_move = 0        # address of next particle to move

        for i in range(self.mult*num_A):           # generate initial positions
            self.pos.append([np.random.random_sample()*15, np.random.random_sample()*15])
            self.posA.append(self.pos[i])
        for j in range (self.mult*num_B):
            self.pos.append([np.random.random_sample()*15, np.random.random_sample()*15])
            self.posB.append(self.pos[self.mult*num_A+j])

        self.E_total = E_harmonic(self.pos, self.kspring) + E_LJ(self.posA, self.posB,
                                                            [self.rcutoffAA, self.rcutoffBB, self.rcutoffAB],
                                                            [self.epsilon_AA, self.epsilon_BB, self.epsilon_AB],
                                                            [self.sigma_A, self.sigma_B, self.sigma_AB])       # calculate initial energy

    def data(self):         # returns all data
        return self.pos, self.posA, self.posB, self.E_total

    def update(self):        # move beads if energetically favourable, return new positions and total energy
        copy = self.pos[self.next_move].copy()    # make copy of old values to revert to if necessary
        
        if self.next_move < self.mult*num_A:         # move particle
            dx = np.random.random_sample() * 0.05 * self.sigma_A * np.random.choice([-1,1])
            dy = np.random.random_sample() * 0.05 * self.sigma_A * np.random.choice([-1,1])
            self.pos[self.next_move][0] += dx
            self.pos[self.next_move][1] += dy
            self.posA[self.next_move][0] += dx
            self.posA[self.next_move][1] += dy
        else:
            dx = np.random.random_sample() * 0.05 * self.sigma_B * np.random.choice([-1,1])
            dy = np.random.random_sample() * 0.05 * self.sigma_B * np.random.choice([-1,1])
            self.pos[self.next_move][0] += dx
            self.pos[self.next_move][1] += dy
            self.posB[self.next_move-self.mult*num_A][0] += dx
            self.posB[self.next_move-self.mult*num_A][1] += dy

        new_E_total = E_harmonic(self.pos, self.kspring) + E_LJ(self.posA, self.posB,
                                                            [self.rcutoffAA, self.rcutoffBB, self.rcutoffAB],
                                                            [self.epsilon_AA, self.epsilon_BB, self.epsilon_AB],
                                                            [self.sigma_A, self.sigma_B, self.sigma_AB])            # calculate new energy
        
        dE = new_E_total - self.E_total
        if dE > 0:                           #if dE < 0, allow, else, use compare exp and random for metropolis monte carlo simulation
            a = np.exp(-dE/self.kT)
            X = np.random.random_sample()
            if X > a:
                self.pos[self.next_move] = copy
                if self.next_move < self.mult*num_A: self.posA[self.next_move] = copy
                else: self.posB[self.next_move-self.mult*10] = copy
                self.next_move += 1
                if self.next_move >= (self.mult*10): self.next_move -= self.mult*10
                return system.pos, system.posA, system.posB, system.E_total

        self.next_move += 1
        if self.next_move >= (self.mult*10): self.next_move -= self.mult*10
        self.E_total = new_E_total
        return system.pos, system.posA, system.posB, system.E_total


def E_harmonic(pos, kspring): #E(i, j) = 0.5*kspring*(x_i-x_j)^2            estimates energy in bonds by approximating them as springs
    E_h = 0
    for i in range(len(pos)-1):
            d = (pos[i][0] - pos[i+1][0])**2 + (pos[i][1] - pos[i+1][1])**2      # distance between 2 particles squared, is (x_i-x_j)^2
            E_h += 0.5*kspring*d
    return E_h

def E_LJ(posA, posB, rcutoff, epsilon, sigma): #V(r) = 4*well_depth[(rad/dist)**12-(rad/dist)**6]    Lennard-Jones potential, estimates energy from pauli repulsion and van der waals forces
    Elj = 0
    [rcutoffAA, rcutoffBB, rcutoffAB] = rcutoff
    [epsilon_AA, epsilon_BB, epsilon_AB] = epsilon
    [sigma_A, sigma_B, sigma_AB] = sigma

    for i,molA1 in enumerate(posA):
        for molA2 in posA[i+1:]:
            r = ((molA1[0]-molA2[0])**2 + (molA1[1]+molA2[1])**2)**0.5
            if r <= rcutoffAA:
                Elj += 4 * epsilon_AA * ((sigma_A/r)**12-(sigma_A/r)**6)
        for molB in posB:
            r = ((molA1[0]-molB[0])**2 + (molA1[1]+molB[1])**2)**0.5
            if r <= rcutoffAB:
                Elj += 4 * epsilon_AB * ((sigma_AB/r)**12-(sigma_AB/r)**6)

    for i,molB1 in enumerate(posB):
        for molB2 in posB[i+1:]:
            r = ((molB1[0]-molB2[0])**2 + (molB1[1]+molB2[1])**2)**0.5
            if r <= rcutoffBB:
                Elj += 4 * epsilon_BB * ((sigma_B/r)**12-(sigma_B/r)**6)
    return Elj

                                                                                    #start generating the beads and positions
num_A = int(input("input the number of A beads in each polymer: "))   #5
system = beads(num_A)
initial_position, initial_positionA, initial_positionB, newETotal = system.data()
TEnergyList = []


n_step = int(input("input the Number of Step: "))
for i in range(n_step): 
    new_pos, new_posA, new_posB, newETotal = system.update()
    TEnergyList.append(newETotal)
    
    screen.fill((0,0,0))
    for line in new_posA:
        pygame.draw.circle(screen,(255,0,0),(int(40*line[0]),int(40*line[1])),5)
    for line in new_posB:
        pygame.draw.circle(screen,(0,0,255),(int(40*line[0]),int(40*line[1])),5)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        elif event.type == KEYDOWN:
            if   event.key == K_ESCAPE:
                pygame.quit()
                exit()
    pygame.display.update()
    fpsClock.tick(90)

'''
xA, yA, xB, yB = [],[],[],[]
for line in new_posA:
    xA.append(line[0])
    yA.append(line[1])
for line in new_posB:
    xB.append(line[0])
    yB.append(line[1])
plt.plot(xA, yA, 'go', label = 'position of beads A')
plt.plot(xB, yB, 'bs', label = 'position of beads B')        
plt.xlabel('x coordinates of beads')
plt.ylabel('y coordinates of beads')
plt.legend()
plt.title('positions of 500 beads')
plt.show()
'''
xE = [a for a in range(n_step)]
yE = TEnergyList
plt.plot(xE, yE, 'ro', label = 'Energy Change')
plt.xlabel('Step Number')
plt.ylabel('Total Energy of the system')
plt.legend()
plt.title('Total Energy of the system')
plt.show()
plt.close()








