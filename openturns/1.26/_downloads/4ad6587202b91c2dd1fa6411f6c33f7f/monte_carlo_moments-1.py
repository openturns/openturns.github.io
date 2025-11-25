import openturns as ot
import openturns.viewer as otv

dist = ot.LogNormal()
dist.setDescription(['Z'])
sample = dist.getSample(100)
graph = dist.drawPDF()
histogram = ot.HistogramFactory().build(sample).drawPDF().getDrawable(0)
histogram.setColor('blue')
graph.add(histogram)
otv.View(graph)