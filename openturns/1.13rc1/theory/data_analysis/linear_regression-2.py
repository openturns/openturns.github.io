import openturns as ot
from openturns.viewer import View

N = 1000
#create a sample X
dist = ot.Triangular(1.0, 5.0, 10.0)
# create a Y sample : Y = exp(X/2) + eps
eps = ot.Normal(0.0, 1.0)
sample = ot.ComposedDistribution([dist, eps]).getSample(N)
f = ot.SymbolicFunction(['x', 'eps'], ['exp(0.5*x)+eps'])
sampleY = f(sample)
sampleX = sample.getMarginal(0)
sampleX.setName('X')
# same as good test
regressionModel = ot.LinearModelAlgorithm(sampleX, sampleY).getResult()
graph = ot.VisualTest.DrawLinearModel(sampleX, sampleY, regressionModel)
cloud = graph.getDrawable(0)
cloud.setPointStyle('times')
graph.setDrawable(cloud, 0)
graph.setTitle('')
View(graph)