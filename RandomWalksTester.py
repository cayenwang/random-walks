# new lattice definition. A lattice is a set of points with only a few qualities: adjacency, edge direction and weighting. adjacency is could 
# be  a function which checks for adjacency or it could be a function that calculates the adjacent points. Take the second option and we have 
# a function which also defines the region we are considering the walks in. Awesome now let the weightings function be none symmetric i.e 
# f(A,B) ≠ f(B,A) and bobs you uncle. let adj stand for adjacency

# biases is a function that takes an ordered touple of nodes and returns the bias in that direction 
# adj is a function that returns all the nodes adjacent to that point 

import numpy as np 
class Lattice: 
    def __init__(self, adj, biases):
        self.adjPoints = adj
        self.biases = biases  
    def pointBias(self, point): 
        edgeBias = []
        for i in self.adjPoints(point): 
            edgeBias.append(self.biases(point,i))
        return edgeBias
    
def planeAdj(v):
    x=v[0]; y=v[1] 
    return [[x+1,y],[x-1,y],[x,y+1],[x,y-1]] # This works woo 

def planeBias(v,w):
    return 0.25
plane = Lattice(planeAdj, planeBias) # probably will change to a function which always outputs 0.25




class RandWalks: 
    def __init__(self, lattice, length, origin = [0,0]): #origin should be a property of the lattice, maybe this should be a sub class of lattice 
        self.origin = origin 
        runDir = [origin]
        runLocation = [0,0]
        self.adjPoints = lattice.adjPoints
        self.pointBias = lattice.pointBias
        for i in range(length): 
            runLocation =self.adjPoints(runLocation)[int(np.random.choice(range(len(self.adjPoints(runLocation))),1 , self.pointBias(runLocation)))] #Error type of input data not int? This isnt the location its the direction we are moving in 
            # ahh the problem is runLocation is a number but it then gets fed back into the adjpoints fucntion as sif its a point which it isnt 
            runDir.append(runLocation) 
        self.runDir = runDir


planeWalk = RandWalks(plane,100)
print(planeWalk.runDir)


