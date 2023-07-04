#import RandomWalksTester as ranWal

def lat2DAdj(v):
    x=v[0]; y=v[1] 
    return [[x+1,y],[x-1,y],[x,y+1],[x,y-1]] # This works woo 

#I have 0 right 1 left 2 up 3 down 4 in 5 out

def lat3DAdj(v): 
    x = v[0]; y = v[1]; z = v[2]
    return [[x +1, y, z], [x-1, y, z], [x, y+1, z], [x, y-1, z], [x, y, z+1], [x, y, z-1] ]

def triGridAdj(v):
    x=v[0]; y=v[1]
    return [[x+1,y],[x-1,y],[x,y+1],[x,y-1], [x+1,y+1], [x-1,y-1]] #to see this is the triangle grid draw one out and then deform the points so 
#they appear to be a square grid. I've ordered the list so paths from the 2d square grid can be translated directly across

def hexGridAdj(v):
    x=v[0]; y=v[1]
    return [[x+1,y],[x,y-1], [x-1,y-1]] # havent checked this properly yet. same method as the triangle grid. Be careful! not every point from 
# the normal lattice is actually included in the hex grid so it does depend on what coordinate you start your path on which hex grid youll be traveling on 

# we want a function which takes two inputs and delivers an output. We want to define it so that it can take information from the adjacency function 
# that it is defined on. so at some point it needs to take the adjacency function as an argument 
# I'm going to explore two Ideas: First just have the bias function reference the adj function I'm going to use it on. all the adj files are defined 
# in this document anyway. Second having biases functions which take a adj function as a bias 


def funnelBias2(v,w):
    funnelAdj = list(filter(lambda x : (x[0] <= abs(x[1])) and (x[0] >= -abs(x[1])), lat2DAdj(v))) # this is right
    if w in funnelAdj: 
        out = 1/len(funnelAdj)
    else: out = 0 
    return out

# this looks at adjacent points and filters out those not in the region to make a new list of adjacent points. if youre on the list you get 
#