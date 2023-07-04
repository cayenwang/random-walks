import RandomWalksTester as ranWal
import LatticePresets as latP
import numpy as np 
#print(len(list(filter(lambda x : (x[0] <= abs(x[1])) and (x[0] >= -abs(x[1])), walk.runDir))))
plane = ranWal.Lattice(latP.lat2DAdj, latP.funnelBias2)
walk = ranWal.RandWalk(plane,5000)
# walk.runDir
print(walk.runNumInt)

