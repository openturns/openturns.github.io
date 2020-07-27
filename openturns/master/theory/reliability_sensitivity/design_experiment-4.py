import openturns as ot
from openturns.viewer import View

# Box
d = ot.Box([3, 4, 5])
s = d.generate()
s.setDescription(["X1", "X2", "X3"])
g = ot.VisualTest.DrawPairs(s)
g.setTitle("Box experiment")
View(g)