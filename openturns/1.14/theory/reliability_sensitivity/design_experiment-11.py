import openturns as ot
from openturns.viewer import View

# Tuples
d = ot.Tuples([3, 4, 5])
s = ot.Sample(d.generate())
s.setDescription(["X1", "X2", "X3"])
g = ot.Graph()
g.setTitle("Tuples generator")
g.setGridColor("black")
p = ot.Pairs(s)
g.add(p)
View(g)