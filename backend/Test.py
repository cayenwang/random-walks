import RandomWalks as ranWal
import LatticePresets as latP
import numpy as np 
#print(len(list(filter(lambda x : (x[0] <= abs(x[1])) and (x[0] >= -abs(x[1])), walk.runDir))))
plane = ranWal.Lattice(latP.lat2DAdj)

numberOfWalks = 1
lengthOfWalks = 100

for i in range(numberOfWalks):
    walk = ranWal.RandWalk(plane,lengthOfWalks)
    print(len(walk.runNumInt),walk.runNumInt)