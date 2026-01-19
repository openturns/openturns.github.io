import openturns as ot
import openturns.viewer as otv
import otmeshing

points = ot.Normal(2).getSample(100)
mesher = otmeshing.ConvexHullMesher()

hull = mesher.build(points)
graph = hull.draw()
graph.add(ot.Cloud(points))
graph.setLegendPosition("upper left")
graph.setTitle("Convex hull of sample")

view = otv.View(graph)
otv.View.ShowAll()
