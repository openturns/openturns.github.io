import openturns as ot
from openturns.viewer import View

ot.RandomGenerator.SetSeed(0)
copula1 = ot.FrankCopula()
data1 = copula1.getSample(1000)
copula2 = ot.ClaytonCopula(2.0)
data2 = copula2.getSample(1000)
graph1 = ot.VisualTest.DrawLowerTailDependenceFunction(data1)
graph1.setTitle('Lower tail dependence function:Frank :')
graph2 = ot.VisualTest.DrawLowerTailDependenceFunction(data2)
graph2.setTitle('Lower tail dependence function: Gumbel(2.0)')
grid3 = ot.GridLayout(1,2)
grid3.setGraph(0,0,graph1)
grid3.setGraph(0,1,graph2)
View(grid3)