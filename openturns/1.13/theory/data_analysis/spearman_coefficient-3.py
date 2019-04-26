import openturns as ot
from openturns.viewer import View

N = 20
ot.RandomGenerator.SetSeed(10)
x = ot.Uniform(0.0, 10.0).getSample(N)
f = ot.SymbolicFunction(['x'], ['5'])
y = ot.Uniform(0.0, 10.0).getSample(N)
graph = f.draw(0.0, 10.0)
graph.setTitle('nSpearman\'s coefficient estimate is close to zero\nbecause U and V are independent')
graph.setXTitle('u')
graph.setYTitle('v')
cloud = ot.Cloud(x, y)
cloud.setPointStyle('circle')
cloud.setColor('orange')
graph.add(cloud)
View(graph)