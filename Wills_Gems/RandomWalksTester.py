# Lattice is defined as a class. Its paramters are two functions adj and biases. Adj takes a node and tells you which nodes are adjacent to it 
# and biases takes two ordered nodes and tells you what the probability of going down the corresponding edge is. this defines the lattice which the 
# walk will happen on. Lattice has 3 class methods adjNode which is equivalent to adj. biases (as youd expect) and nodeBias which takes a node and gives back a list 
# containing all the biases of the paths starting at the given node and leading to adjacent nodes.

# Class RandWalks takes a lattice, length and origin. Origin is where the path will start and is included only to allow for different starting points in irregular 
# lattices later down the road. Lattice must be from the lattice class as the code references adjNode and nodeBias ect. The Line where run location is 
# defined is dodgy and throws up a depreciation error message. I think np.random.choice is giving out a 1d list and its upset im taking that as an integer to make 
# the list call work. I'm sure theres a way to make it the right data type  

import numpy as np 
from operator import add

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

    def __init__(self, lattice, length = 20, origin = [0,0]):
        self.origin = origin 
        runDir = [origin]
        runNumList = []
        runLocation = origin
        self.adjNode = lattice.adjNode
        self.nodeBias = lattice.nodeBias 
        self.length = length

        runNumList, runLocation, runDir = self.generateWalk(runDir, runNumList, runLocation)

        self.runDir = runDir
        self.runNumList = runNumList
        string_value = "".join([str(current_integer) for current_integer in runNumList]) 
        self.runNumInt = int(string_value)

    def generateWalk(self, runDir, runNumList, runLocation):
        for i in range(self.length): 
            x = np.random.choice(range(len(self.adjNode(runLocation))), 1, p = self.nodeBias(runLocation))[0]
            runNumList.append(x)
            runLocation = self.adjNode(runLocation)[x] 
            runDir.append(runLocation)
        return runNumList, runLocation, runDir
            
class selfAvoidantRandWalk(RandWalk):

    def generateWalk(self, runDir, runNumList, runLocation):

        i = 0
        while i < self.length: 
            
            tempBias = self.nodeBias(runLocation)

            flag = True
            while flag == True:

                flag = False
                x = np.random.choice(range(len(self.adjNode(runLocation))), 1, p = tempBias)[0]
                
                tempRunLocation = self.adjNode(runLocation)[x] 

                # if self intersect
                if tempRunLocation in runDir:
                    tempBias[x]=0
                    # if no more options, stop flaging (AND STOP THE WALK)
                    if sum(tempBias) == 0:
                        flag = False
                        i = self.length
                    # if possible options remaining, retry
                    else:
                        tempBias = normalize(tempBias)
                        flag = True
                # if no self intersect, append to list
                else:
                    runLocation = self.adjNode(runLocation)[x] 
                    runNumList.append(x)
                    runDir.append(runLocation)
                    i += 1

        return runNumList, runLocation, runDir

                    

def int2Dir(v):
    numList = list(map(lambda x: int(x), str(v)))
    runLocation = [0,0]
    runDir = [[0,0]]
    for i in numList:
        lookup = {0: [1,0], 1: [-1,0], 2: [0,1], 3: [0,-1]}
        runLocation = [runLocation[0]+lookup[i][0], runLocation[1] + lookup[i][1]]
        runDir.append(runLocation)
    return runDir        #this doesnt work for a leading 0 but it seems to work fine otherwise 

def normalize(v):
    total = sum(v)
    n = v
    for i in range(len(v)):
        n[i]=v[i]/total
    return n
    