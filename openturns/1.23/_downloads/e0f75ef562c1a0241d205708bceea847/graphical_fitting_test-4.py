import openturns as ot
from openturns.viewer import View

ot.RandomGenerator.SetSeed(0)
distribution = ot.LogNormal(2.0, 1.0, 0.0)
sample = distribution.getSample(50)
graph = ot.VisualTest.DrawHenryLine(sample)
View(graph)