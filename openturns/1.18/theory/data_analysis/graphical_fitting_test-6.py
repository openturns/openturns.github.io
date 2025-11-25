import openturns as ot
from openturns.viewer import View

ot.RandomGenerator.SetSeed(0)
copula = ot.FrankCopula(1.5)
copula2 = ot.GumbelCopula(4.5)
sample = copula.getSample(100)
graph = ot.VisualTest.DrawKendallPlot(sample, copula2)
View(graph)