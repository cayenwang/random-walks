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
        self.biases = biases # this line now no longer works 
    def bias(self, point): 
        edgeBias = []
        for i in self.adjPoints(point): 
            edgeBias.append(self.biases(point,i))
        return edgeBias

# This was a basic test case
# def trivAdj(v):
#     return 1 
# trivLat = Lattice(trivAdj,1)
# print(trivLat.adjPoints(13))

def planeAdj(v):
    x=v[0]; y=v[1] 
    return [[x+1,y],[x-1,y],[x,y+1],[x,y-1]] # This works woo 

plane = Lattice(planeAdj, 1/4) # probably will change to a function which always outputs 0.25

class RandWalks: 
    def __init__(self, lattice, length, origin = [0,0]): #origin should be a property of the lattice
        self.origin = origin 
        runDir = [origin]
        runLocation = origin
        for i in range(length): 
            runLocation =np.random.choice(range(len(plane.adjPoints(runLocation))), plane.bias(runLocation))
            runDir.append(runLocation) 
        self.runDir = runDir

# planeWalk = RandWalks(plane,4)
# print(planeWalk.runDir)

