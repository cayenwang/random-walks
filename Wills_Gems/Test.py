import RandomWalksTester as ranWal
import LatticePresets as latP
import numpy as np 
#print(len(list(filter(lambda x : (x[0] <= abs(x[1])) and (x[0] >= -abs(x[1])), walk.runDir))))
plane = ranWal.Lattice(latP.lat2DAdj)

for i in range(100):
    walk = ranWal.selfAvoidantRandWalk(plane,100)
    print(len(str(walk.runNumInt)),walk.runNumInt)