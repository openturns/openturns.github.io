import openturns as ot
from openturns.viewer import View

# GaussProduct
d = ot.GaussProductExperiment(ot.ComposedDistribution([ot.Uniform()]*3), [4,6,8])
s = d.generate()
s.setDescription(["X1", "X2", "X3"])
g = ot.Graph()
g.setTitle("Gauss product experiment")
g.setGridColor("black")
p = ot.Pairs(s)
g.add(p)
View(g)