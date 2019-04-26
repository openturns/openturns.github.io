import openturns as ot
from openturns.viewer import View

# Combinations
d = ot.Combinations(3, 12)
s = ot.Sample(d.generate())
s.setDescription(["X1", "X2", "X3"])
g = ot.Graph()
g.setTitle("Combinations generator")
g.setGridColor("black")
p = ot.Pairs(s)
g.add(p)
View(g)