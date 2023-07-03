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
