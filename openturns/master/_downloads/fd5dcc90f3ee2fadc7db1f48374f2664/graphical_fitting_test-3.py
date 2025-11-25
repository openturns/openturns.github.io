import openturns as ot
import openturns.viewer as otv

ot.RandomGenerator.SetSeed(0)
distribution = ot.Normal(10.0, 2.0)
sample = distribution.getSample(50)
graph = ot.VisualTest.DrawHenryLine(sample)
otv.View(graph)