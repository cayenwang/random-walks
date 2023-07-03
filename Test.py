import numpy as np 
class Lattice: 
    def __init__(self, adj, biases = None):
        if biases is None :
            def biases(v,w):
                return 1/len(adj(v))
        self.adjNode = adj
        self.biases = biases  
    def nodeBias(self, node): 
        edgeBias = []
        for i in self.adjNode(node): 
            edgeBias.append(self.biases(node,i))
        return edgeBias
    
class RandWalk: 
    def __init__(self, lattice, length, origin = [0,0]): #origin should be defined relative to lattice somehow
        self.origin = origin 
        runDir = [origin]
        runNumList = []
        runLocation = origin
        self.adjNode = lattice.adjNode
        self.nodeBias = lattice.nodeBias
        for i in range(length): 
            x = np.random.choice(range(len(self.adjNode(runLocation))),1 , self.nodeBias(runLocation))[0]
            runNumList.append(x)
            runLocation =self.adjNode(runLocation)[np.random.choice(range(len(self.adjNode(runLocation))),1 , self.nodeBias(runLocation))[0]] 
            runDir.append(runLocation) 
        self.runDir = runDir
        self.runNumList = runNumList
        string_value = "".join([str(current_integer) for current_integer in runNumList]) # this takes the list of integers turns it into a list
        # of strings and then joins them and returns an integer
        self.runNumInt = int(string_value)
        
def lat2DAdj(v):
    x=v[0]; y=v[1] 
    return [[x+1,y],[x-1,y],[x,y+1],[x,y-1]] # This works woo 


def lat2DBias(v,w):
    return 0.25

plane = Lattice(lat2DAdj)
rand = RandWalk(plane, 8)
print(rand.runNumInt)

#Time to figure out a const function which assigns a given probability to every edge so ther edoesnt have to be a unique constant function for everything
