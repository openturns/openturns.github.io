import openturns as ot
from openturns.viewer import View

# MonteCarlo
d = ot.MonteCarloExperiment(ot.JointDistribution([ot.Uniform()]*3), 32)
s = d.generate()
s.setDescription(["X1", "X2", "X3"])
g = ot.VisualTest.DrawPairs(s)
g.setTitle("MonteCarlo experiment")
View(g)