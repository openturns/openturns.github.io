import openturns as ot
from openturns.viewer import View

# Box
d = ot.Box([3, 4, 5])
s = d.generate()
s.setDescription(["X1", "X2", "X3"])
g = ot.Graph()
g.setTitle("Box experiment")
g.setGridColor("black")
p = ot.Pairs(s)
g.add(p)
View(g)