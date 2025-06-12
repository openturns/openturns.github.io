import openturns as ot
import openturns.viewer as otv
from openturns.usecases import flood_model

fm = flood_model.FloodModel()
heightInputDistribution, heightModel = fm.getHeightModel()

# %%
# Set all inputs to constants, except Q
indices = [1, 2, 3]
referencePoint = [heightInputDistribution.getMarginal(i).getMean()[0] for i in indices]
heightModelvsQ = ot.ParametricFunction(heightModel, indices, referencePoint)
qRange = fm.Q.getRange()
qMin = qRange.getLowerBound()[0]
qMax = qRange.getUpperBound()[0]
graph = heightModelvsQ.draw(qMin, qMax, 200)
otv.View(graph)