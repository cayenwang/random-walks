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
    if v == [1,0]: return 4
    return 0.25
plane = Lattice(planeAdj, planeBias) # probably will change to a function which always outputs 0.25
planeBias(23,34)
plane.biases(1,2)
plane.pointBias([1,2])
