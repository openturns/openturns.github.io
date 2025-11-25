import openturns as ot
import openturns.viewer as otv

# Box
d = ot.Box([3, 4, 5])
s = d.generate()
s.setDescription(["X1", "X2", "X3"])
g = ot.VisualTest.DrawPairs(s)
g.setTitle("Box experiment")
otv.View(g)