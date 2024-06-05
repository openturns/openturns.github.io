import openturns as ot
from openturns.viewer import View

# Sobol
d = ot.LowDiscrepancyExperiment(ot.SobolSequence(), ot.JointDistribution([ot.Uniform()]*3), 32)
s = d.generate()
s.setDescription(["X1", "X2", "X3"])
g = ot.VisualTest.DrawPairs(s)
g.setTitle("Low discrepancy experiment")
View(g)