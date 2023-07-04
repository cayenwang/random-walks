# Lattice is defined as a class. Its paramters are two functions adj and biases. Adj takes a node and tells you which nodes are adjacent to it 
# and biases takes two ordered nodes and tells you what the probability of going down the corresponding edge is. this defines the lattice which the 
# walk will happen on. Lattice has 3 class methods adjNode which is equivalent to adj. biases (as youd expect) and nodeBias which takes a node and gives back a list 
# containing all the biases of the paths starting at the given node and leading to adjacent nodes.

#Class  RandWalks takes a lattice, length and origin. Origin is where the path will start and is included only to allow for different starting points in irregular 
# lattices later down the road. Lattice must be from the lattice class as the code references adjNode and nodeBias ect. The Line where run location is 
# defined is dodgy and throws up a depreciation error message. I think np.random.choice is giving out a 1d list and its upset im taking that as an integer to make 
# the list call work. I'm sure theres a way to make it the right data type  

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

# This seems to work fine 

class RandWalk: 
    def __init__(self, lattice, length = 20, origin = [0,0]): #origin should be defined relative to lattice somehow
        self.origin = origin 
        runDir = [origin]
        runNumList = []
        runLocation = origin
        self.adjNode = lattice.adjNode
        self.nodeBias = lattice.nodeBias   # these both work 
        for i in range(length): 
            x = np.random.choice(range(len(self.adjNode(runLocation))),1 , p = self.nodeBias(runLocation))[0]
            runNumList.append(x)
            runLocation =self.adjNode(runLocation)[np.random.choice(range(len(self.adjNode(runLocation))),1 , p= self.nodeBias(runLocation))[0]] 
            runDir.append(runLocation) 
        self.runDir = runDir
        self.runNumList = runNumList
        string_value = "".join([str(current_integer) for current_integer in runNumList]) # this takes the list of integers turns it into a list
        # of strings and then joins them and returns an integer
        self.runNumInt = int(string_value)
        
