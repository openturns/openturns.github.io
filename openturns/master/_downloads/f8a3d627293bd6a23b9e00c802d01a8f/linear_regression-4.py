import openturns as ot
from openturns.viewer import View

N = 1000
#create a sample X
dist = ot.Triangular(1.0, 5.0, 10.0)
# create a Y sample : Y = exp(X/2) + eps
eps = ot.Normal(0.0, 1.0)
sample = ot.JointDistribution([dist, eps]).getSample(N)
f = ot.SymbolicFunction(['x', 'eps'], ['exp(0.5*x)+eps'])
sampleY = f(sample)
sampleX = sample.getMarginal(0)
sampleX.setName('X')
# same as good test
regressionModel = ot.LinearModelAlgorithm(sampleX, sampleY).getResult()
graph = ot.VisualTest.DrawLinearModelResidual(regressionModel)
cloud = graph.getDrawable(0)
cloud.setPointStyle('times')
graph.setDrawable(0, cloud)
graph.setTitle('')
View(graph)