import openturns as ot
import openturns.viewer as otv
from openturns.usecases import flood_model

fm = flood_model.FloodModel()

# Set all inputs to constants, except Hd
indices = [0, 1, 2, 3, 4, 5, 6]
referencePoint = [fm.distribution.getMarginal(i).getMean()[0] for i in indices]
costModelvsHd = ot.ParametricFunction(fm.model.getMarginal(2), indices, referencePoint)
hdMin = 0.0
hdMax = 12.0
graph = costModelvsHd.draw(hdMin, hdMax, 200)
otv.View(graph)