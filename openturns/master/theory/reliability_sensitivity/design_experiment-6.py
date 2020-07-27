import openturns as ot
from openturns.viewer import View

# LHS
d = ot.LHSExperiment(ot.ComposedDistribution([ot.Uniform()]*3), 32)
s = d.generate()
s.setDescription(["X1", "X2", "X3"])
g = ot.VisualTest.DrawPairs(s)
g.setTitle("LHS experiment")
View(g)