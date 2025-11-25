import openturns as ot
from openturns.viewer import View

N = 5
ot.RandomGenerator.SetSeed(0)
x = ot.Uniform(2.0, 8.0).getSample(N)
f = ot.SymbolicFunction(['x'], ['80-0.4*(x-2)^3'])
y = f(x) + ot.Normal(0.0, 20.0).getSample(N)
graph = f.draw(2.0, 8.0)
graph.setTitle('Non significant Spearman coefficient')
graph.setXTitle('u')
graph.setYTitle('v')
cloud = ot.Cloud(x, y)
cloud.setPointStyle('circle')
cloud.setColor('orange')
graph.add(cloud)
View(graph)