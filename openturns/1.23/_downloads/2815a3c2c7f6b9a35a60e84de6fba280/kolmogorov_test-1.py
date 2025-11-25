import openturns as ot
from matplotlib import pyplot as plt
from openturns.viewer import View

candidate = ot.Exponential(0.07, 0.0)
graph = candidate.drawCDF(0.0, 30.0)

sample = ot.Sample([[5.0], [6.0], [10.0], [22.0], [27.0]])
empiricalDrawable = ot.UserDefined(sample).drawCDF(0.0, 30.0).getDrawable(0)
empiricalDrawable.setColor('darkblue')
graph.add(empiricalDrawable)

graph.setTitle('CDF comparison')
graph.setLegends(['Candidate CDF', 'Empirical CDF'])
View(graph)