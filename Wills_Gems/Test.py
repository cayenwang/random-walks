import RandomWalksTester as ranWal
import LatticePresets as latP
import numpy as np 
#print(len(list(filter(lambda x : (x[0] <= abs(x[1])) and (x[0] >= -abs(x[1])), walk.runDir))))
plane = ranWal.Lattice(latP.lat2DAdj)

numberOfWalks = 30
lengthOfWalks = 100

for i in range(numberOfWalks):
    walk = ranWal.selfAvoidantRandWalk(plane,lengthOfWalks)
    if len(walk.runNumInt) != lengthOfWalks:
        print(len(walk.runNumInt),walk.runNumInt)