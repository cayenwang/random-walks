import RandomWalksTester as ranWal
import LatticePresets as latP
import numpy as np 

plane = ranWal.Lattice(latP.lat2DAdj, latP.funnelBias2)
walk = ranWal.RandWalk(plane,200)
print(walk.runDir)
print(walk.runNumInt)

