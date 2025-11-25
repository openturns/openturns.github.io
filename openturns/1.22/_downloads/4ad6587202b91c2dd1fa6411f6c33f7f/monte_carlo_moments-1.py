import openturns as ot
from openturns.viewer import View

dist = ot.LogNormal()
dist.setDescription(['Z'])
sample = dist.getSample(100)
graph = dist.drawPDF()
histogram = ot.HistogramFactory().build(sample).drawPDF().getDrawable(0)
histogram.setColor('blue')
graph.add(histogram)
View(graph)