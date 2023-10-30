import openturns as ot
import openturns.viewer as otv
import pylab as pl
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
view = otv.View(
    graph,
    figure_kw={"figsize": (6.0, 4.0)},
    legend_kw={"bbox_to_anchor": (1.0, 1.0), "loc": "upper left"},
)
pl.subplots_adjust(right=0.7)