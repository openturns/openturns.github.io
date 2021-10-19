import openturns as ot
from openturns.viewer import View

N = 5
ot.RandomGenerator.SetSeed(0)
x = ot.Uniform(0.0, 8.0).getSample(N)
f = ot.SymbolicFunction(['x'], ['15*x+1'])
y = f(x) + ot.Normal(0.0, 20.0).getSample(N)
graph = f.draw(0.0, 8.0)
graph.setTitle('Non significant Pearson coefficient')
graph.setXTitle('u')
graph.setYTitle('v')
cloud = ot.Cloud(x, y)
cloud.setPointStyle('circle')
cloud.setColor('orange')
graph.add(cloud)
View(graph)