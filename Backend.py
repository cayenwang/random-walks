# make a class called random walks which includes the parameters: lattice ( for the lattice the random walk is travelling on), origin, 
# (dynamically changeing bias?)is going to be a pain. also length dummy

# class RandWalks: 
#     def __init__(self, lattice, length, origin = 0)
#     # not sure how we are going to deal with this origin parameter in the future. want to have the 
#     # default argument to be the origin of whatever lattice we are considering
#     self.origin = origin 
#     # we have a lattice param that tells us all the liklihoods of the different walks so we need to know where we are at all times 
#     # lattice variable is going to be a variable depending on the lattice to encode the amount of choices you can make at that point 
#     # LatticeWeightsAtX will be a list bassed on the position in lattice weights 
#     np.random.choice(range('latticeVarDirections'), 'LatticeWeightsAtX' )

# What is lattice? its a matrix with each cell representing a point. In theres a cell theres an array hich represents the weightings of all
# the paths going out of it. It also has to tell use where the weightings lead to ooof. so its better to treat it as somesort of nested 
# dictionary? how are we going to define this iteratively oooof

# IMPORTANT instead of using look ups going to only consider the function case. Not going to decide how to define coordinates or anything about
#  the lattice because its confusing 

# the lattice is only going to act on a region but we keep the path in the region using the function by defining certain edges to be equal to 0 
# import numpy as np
# class Lattice:
#     def __init__(self, edges, biases):
#         def edge(v):
#             return edges[v]
#         def bias(v):
#             biasAtV = []
#             for w in edge(v):
#                 biasAtV.append(biases(w))
#             return biasAtV 

# so the class lattice takes two functions edges and biases. gives the edges connected to each node v and then defines the bias associated with each edge 
# to define bias it might be easier to define a real value to each edge and then calculate ratios of each edge to work out the probability than assigning 
# each edge individually 



class RandWalks: 
    def __init__(self, lattice, length, origin = 0):
        self.origin = origin 
        run = [origin]
        runLocation = origin
        for i in range(length): 
            runLocation = 


    np.random.choice(range('latticeVarDirections'), 'LatticeWeightsAtX' )



    import numpy as np 
class Lattice: 
    def adjPoints(self, v ,adj):
        return adj(v)
    def bias(self,v, biases):
        biasAtV = []
        for w in self.adjPoints(v):
            biasAtV.append(biases(v,w))
        return biasAtV

def trivAdj(v):
    return 1 
trivLat = Lattice(trivAdj,1)
trivLat.adjPoints(13)

# def planeAdj(v):
#     x=v[0]; y=v[1] 
#     return [[x+1,y],[x-1,y],[x,y+1],[x,y-1]] # This works woo 

# plane = Lattice(planeAdj, 1/4) # probably will change to a function which always outputs 0.25

# class RandWalks: 
#     def __init__(self, lattice, length, origin = [0,0]): #origin should be a property of the lattice
#         self.origin = origin 
#         runDir = [origin]
#         runLocation = origin
#         for i in range(length): 
#             runLocation =np.random.choice(range(len(plane.adjPoints(runLocation))), plane.bias(runLocation))
#             runDir.append(runLocation) 
#         self.runDir = runDir

# planeWalk = RandWalks(plane,4)
# print(planeWalk.runDir)

