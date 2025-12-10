import openturns as ot
import openturns.viewer as otv
import otmeshing

points = ot.JointDistribution([ot.Uniform()] * 2).getSample(15)
mesher = otmeshing.CloudMesher()

triangulation = mesher.build(points)
graph = triangulation.draw()
graph.setLegendPosition("upper left")
graph.setTitle("Triangulation of sample")

view = otv.View(graph)
otv.View.ShowAll()
