import openturns as ot
from openturns.viewer import View

ot.RandomGenerator.SetSeed(0)
distribution = ot.Normal(3.0, 3.0)
distribution2 = ot.Normal(2.0, 1.0)
sample = distribution.getSample(150)
graph = ot.VisualTest.DrawQQplot(sample, distribution2)
View(graph)