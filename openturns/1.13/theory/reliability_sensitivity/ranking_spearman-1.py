import openturns as ot
from matplotlib import pyplot as plt
from openturns.viewer import View
size = 6
ot.RandomGenerator.SetSeed(3)

# Data
x1 = ot.Uniform(1.0, 9.0).getSample(size)
y1 = ot.Uniform(0.0, 120.0).getSample(size)
graph = ot.Graph("Non significant Spearman coefficient", "u", "v", True, "")
cloud1 = ot.Cloud(x1, y1)
cloud1.setPointStyle("diamond")
cloud1.setColor("orange")
cloud1.setLineWidth(2)
graph.add(cloud1)

size = 150 - size

# Data
x2 = ot.Uniform(1.0, 9.0).getSample(size)
y2 = ot.Uniform(0.0, 120.0).getSample(size)
# Merge with previous data
x = ot.Sample(x1)
y = ot.Sample(y1)
x.add(x2)
y.add(y2)
# Quadratic model
algo = ot.QuadraticLeastSquares(x, y)
algo.run()
quadratic = algo.getMetaModel()

graph = ot.Graph("Null Spearman coefficient", "u", "v", True, "")
graph.add(cloud1)
cloud2 = ot.Cloud(x2, y2)
cloud2.setPointStyle("square")
cloud2.setColor("blue")
cloud2.setLineWidth(2)
graph.add(cloud2)
curve2 = ot.Curve(x, quadratic(x))
curve2.setColor("black")
curve2.setLineWidth(2)
graph.add(curve2)

View(graph)