#step:
# t = 3s start of step has x3 and v2.5
# 0. generate new copy of Space
# 1. find E3, B3, p3
# 2. advance v2.5 to v3.5 for new Space
# 3. advance x3 to x4 for new Space
# 4. aggregate old Space, store that, then delete old Space


class Space:
    def __init__(self, size, edge = 1, defaultstep = 0):
        self.particles = []
        self.cells = []
        self.size = size # array of ints representing the dimensions of the space
        self.edge = edge
        self.defaultstep = defaultstep
        self.dimensions = len(size)
    def step(self, t):
        # act on particles for time t
## need details here

class Particle:
    def __init__(self, ptype, ptypes, velocity, momentum, position):
        if(ptype == "electron"):
            self.mass = ptypes["electron"].mass
            self.charge = ptypes["electron"].charge
            #etc
        self.velocity = velocity
        self.momentum = momentum
        self.position = position
        self.KE = 0.5*self.mass*(self.velocity*self.velocity)

    def calculateValues(self):
        self.calculateKE()
        #etc

    def calculateKE(self):
        self.KE = self.KE + 0.5*self.mass*"velocity^2"

class Vector:
    def __init__(self, vectorComponents):
        self.vectorComponents = vectorComponents

    def addVector(self, oVector):
        self.vectorComponents[0] += oVector.vectorComponents[0]

    def __mult__(self, oVector):
        dummy = 0
        for i in range(0:2) # 2-D problem, for now
           dummy += self.vector[i]*oVector[i]
        return dummy

class Cell:
    def __init__(self, location):
        self.location = location # array of ints representing its location in space
        self.particles = []
        self.node = [] # the size depends on the number of dimensions

    def insertParticle(self, particle):
        self.particles.append(particle)
        # update node values
    def calculateNodeValues(self):
        # calculate the new node values now that particles have moved
        
