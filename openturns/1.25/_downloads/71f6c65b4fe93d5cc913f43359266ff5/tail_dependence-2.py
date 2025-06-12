import openturns as ot
from openturns.viewer import View

ot.RandomGenerator.SetSeed(0)
copula1 = ot.FrankCopula()
data1 = copula1.getSample(1000)
copula2 = ot.GumbelCopula(2.0)
data2 = copula2.getSample(1000)
graph1 = ot.VisualTest.DrawUpperExtremalDependenceFunction(data1)
graph1.setTitle('Upper extremal dependence function: Frank')
graph2 = ot.VisualTest.DrawUpperExtremalDependenceFunction(data2)
graph2.setTitle('Upper extremal dependence function: Gumbel(2.0)')
grid2 = ot.GridLayout(1,2)
grid2.setGraph(0,0,graph1)
grid2.setGraph(0,1,graph2)
View(grid2)