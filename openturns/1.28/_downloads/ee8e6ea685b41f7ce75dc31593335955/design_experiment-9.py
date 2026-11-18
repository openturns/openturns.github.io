import openturns as ot
import openturns.viewer as otv

# Combinations
d = ot.Combinations(3, 12)
s = ot.Sample(d.generate())
s.setDescription(["X1", "X2", "X3"])
g = ot.VisualTest.DrawPairs(s)
g.setTitle("Combinations generator")
otv.View(g)