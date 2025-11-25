import openturns as ot
import openturns.viewer as otv
from matplotlib import pyplot as plt
from openturns.usecases import flood_model

fm = flood_model.FloodModel()
heightInputDistribution, heightModel = fm.getHeightModel()
outputDimension = heightModel.getOutputDimension()

sampleSize = 2**13
sie = ot.SobolIndicesExperiment(heightInputDistribution, sampleSize)
inputDesign = sie.generate()
input_names = heightInputDistribution.getDescription()
inputDesign.setDescription(input_names)
inputDesign.getSize()
outputDesign = heightModel(inputDesign)

# Make a plot
sensitivityAnalysis = ot.SaltelliSensitivityAlgorithm(
    inputDesign, outputDesign, sampleSize
)
graph = sensitivityAnalysis.draw()
graph.setTitle("Height model with (Q, K_s, Z_v, Z_m) as inputs")
graph.setLegendCorner([1.0, 1.0])
graph.setLegendPosition('upper left')
view = otv.View(
    graph,
    figure_kw={"figsize": (6.0, 4.0)},
)
plt.subplots_adjust(right=0.7)