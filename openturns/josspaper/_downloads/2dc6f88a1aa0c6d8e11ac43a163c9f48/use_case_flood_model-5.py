import openturns as ot
import openturns.viewer as otv
from matplotlib import pyplot as plt
from openturns.usecases import flood_model

fm = flood_model.FloodModel(distributionHdLow=False)

outputDimension = fm.model.getOutputDimension()

# Make a plot
sampleSize = 1000
inputSample = fm.distribution.getSample(sampleSize)
outputSample = fm.model(inputSample)
grid = ot.GridLayout(1, outputDimension)
for i in range(outputDimension):
    marginalOutputSample = outputSample.getMarginal(i)
    graph = ot.HistogramFactory().build(marginalOutputSample).drawPDF()
    graph.setLegends([""])
    if i > 0:
        graph.setYTitle("")
    grid.setGraph(0, i, graph)

grid.setTitle("Default scenario: dyke is high")
_ = otv.View(grid, figure_kw={"figsize": (8.0, 2.5)})
plt.subplots_adjust(wspace=0.4, top=0.8)