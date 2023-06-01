import openturns as ot
from openturns.viewer import View

ot.RandomGenerator.SetSeed(0)
distribution = ot.Normal(3.0, 2.0)
sample = distribution.getSample(150)
graph = ot.VisualTest.DrawQQplot(sample, distribution)
View(graph)