import openturns as ot
from openturns.viewer import View

# MonteCarlo
d = ot.MonteCarloExperiment(ot.ComposedDistribution([ot.Uniform()]*3), 32)
s = d.generate()
s.setDescription(["X1", "X2", "X3"])
g = ot.Graph()
g.setTitle("MonteCarlo experiment")
g.setGridColor("black")
p = ot.Pairs(s)
g.add(p)
View(g)