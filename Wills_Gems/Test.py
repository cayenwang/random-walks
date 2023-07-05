import RandomWalksTester as ranWal
import LatticePresets as latP
import numpy as np 
#print(len(list(filter(lambda x : (x[0] <= abs(x[1])) and (x[0] >= -abs(x[1])), walk.runDir))))
plane = ranWal.Lattice(latP.lat2DAdj, latP.funnelBias2D)

walk1 = ranWal.RandWalk(plane,10)
print(walk1.runNumInt)
walk2 = ranWal.selfAvoidantRandWalk(plane,10)
print(walk2.runNumInt)