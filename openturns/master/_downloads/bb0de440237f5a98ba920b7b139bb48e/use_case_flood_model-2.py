import openturns as ot
import openturns.viewer as otv
import pylab as pl
from openturns.usecases import flood_model

fm = flood_model.FloodModel()

sampleSize = 10000
experiment = ot.LowDiscrepancyExperiment(ot.SobolSequence(), fm.distribution, sampleSize, True)
inputSample = experiment.generate()
outputSample = fm.model(inputSample)

graph = ot.Graph("Scenario: dyke is low", "S", "C", True)
cloud = ot.Cloud(outputSample[:, 1], outputSample[:, 2])
graph.add(cloud)
otv.View(graph)