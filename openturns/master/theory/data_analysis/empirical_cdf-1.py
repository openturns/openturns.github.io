import openturns as ot
from matplotlib import pyplot as plt
from openturns.viewer import View

sample = [[5.0], [6.0], [10.0], [22.0], [27.0]]
xmin = 0.0
xmax = 30.0
graph = ot.UserDefined(sample).drawCDF(xmin, xmax)
graph.setTitle('Empirical CDF')
View(graph)