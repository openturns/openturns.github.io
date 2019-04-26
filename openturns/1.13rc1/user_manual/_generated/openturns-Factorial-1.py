import openturns as ot
from matplotlib import pyplot as plt
from openturns.viewer import View

# Generate sample with the given plane
center = [0.5, 1.5]
levels = [4, 8, 16]

experiment = ot.Factorial(center, levels)
sample = experiment.generate()

# Create the graph
graph = ot.Graph(sample.getName(), "x1", "x2", True, "")
cloud = ot.Cloud(sample, "blue", "fsquare", "")
graph.add(cloud)

# Draw the graph
fig = plt.figure(figsize=(4, 4))
axis = fig.add_subplot(111)
View(graph, figure=fig, axes=[axis], add_legend=False, square_axes=True)
axis.set_xlim(auto=True)