import openturns as ot
import openturns.viewer as otv

# KPermutations
d = ot.KPermutations(3, 12)
s = ot.Sample(d.generate())
s.setDescription(["X1", "X2", "X3"])
g = ot.VisualTest.DrawPairs(s)
g.setTitle("KPermutations generator")
otv.View(g)