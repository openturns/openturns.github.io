import openturns as ot
import openturns.viewer as otv

# Composite
d = ot.Composite([1.5, 2.5, 3.5], [1, 2, 3])
s = d.generate()
s.setDescription(["X1", "X2", "X3"])
g = ot.VisualTest.DrawPairs(s)
g.setTitle("Composite experiment")
otv.View(g)