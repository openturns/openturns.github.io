import openturns as ot
from openturns.viewer import View

# Sobol
d = ot.LowDiscrepancyExperiment(ot.SobolSequence(), ot.ComposedDistribution([ot.Uniform()]*3), 32)
s = d.generate()
s.setDescription(["X1", "X2", "X3"])
g = ot.Graph()
g.setTitle("Low discrepancy experiment")
g.setGridColor("black")
p = ot.Pairs(s)
g.add(p)
View(g)