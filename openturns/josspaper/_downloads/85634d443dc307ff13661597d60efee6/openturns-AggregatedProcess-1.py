import openturns as ot
from matplotlib import pyplot as plt
import openturns.viewer as otv

ot.RandomGenerator.SetSeed(0)
if "AggregatedProcess" == "Process":
    # default to Gaussian for the interface class
    process = ot.GaussianProcess()
elif "AggregatedProcess" == "DiscreteMarkovChain":
    process = ot.AggregatedProcess()
    process.setTransitionMatrix(ot.SquareMatrix([[0.0,0.5,0.5],[0.7,0.0,0.3],[0.8,0.0,0.2]]))
    origin = 0
    process.setOrigin(origin)
else:
    process = ot.AggregatedProcess()
process.setTimeGrid(ot.RegularGrid(0.0, 0.02, 50))
process.setDescription(["$x$"])
sample = process.getSample(6)
sample_graph = sample.drawMarginal(0)
sample_graph.setTitle(str(process))

fig = plt.figure(figsize=(10, 4))
sample_axis = fig.add_subplot(111)
otv.View(sample_graph, figure=fig, axes=[sample_axis], add_legend=False)