import openturns as ot
from openturns.viewer import View

ot.RandomGenerator.SetSeed(0)
copula = ot.FrankCopula()
data = copula.getSample(1000)
graph1 = ot.VisualTest.DrawUpperTailDependenceFunction(data)
View(graph1)