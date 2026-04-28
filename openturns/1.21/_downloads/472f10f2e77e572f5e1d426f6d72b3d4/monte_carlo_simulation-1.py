import openturns as ot
from matplotlib import pyplot as plt
from openturns.viewer import View

f = ot.SymbolicFunction(['x'], ['17-exp(0.1*(x-1.0))'])
graph = f.draw(0.0, 12.0)

dist = ot.Normal([5.0, 15.0], [1.0, 0.25], ot.IdentityMatrix(2))
N = 1000
sample = dist.getSample(N)
sample1 = ot.Sample(0, 2)
sample2 = ot.Sample(0, 2)
for X in sample:
    x, y = X
    if f([x])[0] > y:
        sample1.add(X)
    else:
        sample2.add(X)

cloud = ot.Cloud(sample1)
cloud.setColor('green')
cloud.setPointStyle('square')
graph.add(cloud)

cloud = ot.Cloud(sample2)
cloud.setColor('red')
cloud.setPointStyle('square')
graph.add(cloud)

graph.setTitle('Monte Carlo simulation (Pf=0.048, N=1000)')
graph.setLegends(['domain Df', 'simulations'])
graph.setLegendPosition('topright')
View(graph)