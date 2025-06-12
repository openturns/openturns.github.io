import openturns as ot
from openturns.viewer import View

ot.RandomGenerator.SetSeed(0)
copula1 = ot.FrankCopula()
data1 = copula1.getSample(1000)
copula2 = ot.ClaytonCopula(2.0)
data2 = copula2.getSample(1000)
graph1 = ot.VisualTest.DrawLowerExtremalDependenceFunction(data1)
graph1.setTitle('Lower extremal dependence function for the Frank copula')
graph2 = ot.VisualTest.DrawLowerExtremalDependenceFunction(data2)
graph2.setTitle('Lower extremal dependence function for the Clayton(2.0) copula')
grid4 = ot.GridLayout(1,2)
grid4.setGraph(0,0,graph1)
grid4.setGraph(0,1,graph2)
View(grid4)