import openturns as ot
from openturns.viewer import View

# Tuples
d = ot.Tuples([3, 4, 5])
s = ot.Sample(d.generate())
s.setDescription(["X1", "X2", "X3"])
g = ot.VisualTest.DrawPairs(s)
g.setTitle("Tuples generator")
View(g)