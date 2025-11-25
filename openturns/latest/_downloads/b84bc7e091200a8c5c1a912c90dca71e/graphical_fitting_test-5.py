import openturns as ot
import openturns.viewer as otv

ot.RandomGenerator.SetSeed(0)
copula = ot.FrankCopula(1.5)
sample = copula.getSample(100)
graph = ot.VisualTest.DrawKendallPlot(sample, copula)
otv.View(graph)