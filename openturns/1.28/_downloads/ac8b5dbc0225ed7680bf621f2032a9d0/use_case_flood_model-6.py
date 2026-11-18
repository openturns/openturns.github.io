import openturns as ot
import openturns.viewer as otv
from matplotlib import pyplot as plt
from openturns.usecases import flood_model

fm = flood_model.FloodModel()
outputDimension = fm.model.getOutputDimension()

sampleSize = 2**13
sie = ot.SobolIndicesExperiment(fm.distribution, sampleSize)
inputDesign = sie.generate()
input_names = fm.distribution.getDescription()
inputDesign.setDescription(input_names)
inputDesign.getSize()
outputDesign = fm.model(inputDesign)

# Make a plot
grid = ot.GridLayout(outputDimension, 1)
grid.setTitle(f"n = {sampleSize}")
for i in range(outputDimension):
    marginalOutputSample = outputDesign.getMarginal(i)
    sensitivityAnalysis = ot.SaltelliSensitivityAlgorithm(
        inputDesign, marginalOutputSample, sampleSize
    )
    graph = sensitivityAnalysis.draw()
    graph.setTitle(marginalOutputSample.getDescription()[0])
    grid.setGraph(i, 0, graph)
grid.setTitle("Default scenario: dyke is low")
view = otv.View(
    grid,
    figure_kw={"figsize": (7.0, 9.0)},
    legend_kw={"bbox_to_anchor": (1.0, 1.0), "loc": "upper left"},
)
plt.subplots_adjust(wspace=0.4, hspace=0.5, right=0.7)