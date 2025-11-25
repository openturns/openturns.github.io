import openturns as ot
from openturns.viewer import View

# GaussProduct
d = ot.GaussProductExperiment(ot.ComposedDistribution([ot.Uniform()]*3), [4,6,8])
s = d.generate()
s.setDescription(["X1", "X2", "X3"])
g = ot.VisualTest.DrawPairs(s)
g.setTitle("Gauss product experiment")
View(g)