import openturns as ot
import openturns.viewer as otv

# LHS
d = ot.LHSExperiment(ot.JointDistribution([ot.Uniform()]*3), 32)
s = d.generate()
s.setDescription(["X1", "X2", "X3"])
g = ot.VisualTest.DrawPairs(s)
g.setTitle("LHS experiment")
otv.View(g)