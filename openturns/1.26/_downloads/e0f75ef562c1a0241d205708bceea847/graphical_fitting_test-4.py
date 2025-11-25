import openturns as ot
import openturns.viewer as otv

ot.RandomGenerator.SetSeed(0)
distribution = ot.LogNormal(2.0, 1.0, 0.0)
sample = distribution.getSample(50)
graph = ot.VisualTest.DrawHenryLine(sample)
otv.View(graph)