import openturns as ot
import openturns.viewer as otv
import otmeshing

a = [-4.0] * 3
b = [4.0] * 3
f = ot.SymbolicFunction(["x0", "x1"], ["cos(pi_*x0)*sin(pi_*x1)^2"])
f.setInputDescription([r"$x_0$", r"$x_1$"])
f.setOutputDescription([r"$x_2$"])
inputInterval = ot.Interval([a[0], a[1]], [b[0], b[1]])
inputDiscretization = [16] * 2
mesher = otmeshing.FunctionGraphMesher(inputInterval, inputDiscretization)
outputIndex = 2
mesh = mesher.build(f, outputIndex, a[2], b[2])

shading = True
thetaX, thetaY, thetaZ = 6.1, 3.7, 4.3
drawEdge = True
graph = mesh.draw3D(drawEdge, thetaX, thetaY, thetaZ, shading)
graph.setLegendPosition("upper left")
graph.setTitle("Function graph")

view = otv.View(graph)
otv.View.ShowAll()
