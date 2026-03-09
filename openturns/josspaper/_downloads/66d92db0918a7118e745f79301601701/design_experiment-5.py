import openturns as ot
import openturns.viewer as otv

# MonteCarlo
d = ot.MonteCarloExperiment(ot.JointDistribution([ot.Uniform()]*3), 32)
s = d.generate()
s.setDescription(["X1", "X2", "X3"])
g = ot.VisualTest.DrawPairs(s)
g.setTitle("MonteCarlo experiment")
otv.View(g)