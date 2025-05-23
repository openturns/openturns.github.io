import openturns as ot
from openturns.viewer import View

ot.ResourceMap.SetAsUnsignedInteger("Contour-DefaultLevelsNumber", 10)
grid = ot.GridLayout(2, 2)
pdf_graph = ot.Graph("PDFs of 1D Dirichlet distributions", "x", "", True)
cdf_graph = ot.Graph("CDFs of 1D Dirichlet distributions", "x", "", True)
title_2d = "PDF of the Dirichlet dist. with theta = {}"
theta_1 = (2.0, 2.0, 2.0)
theta_2 = (0.5, 0.7, 0.9)
pdf_2d_1 = ot.Graph(title_2d.format(theta_1), "x1", "x2", True)
pdf_2d_2 = ot.Graph(title_2d.format(theta_2), "x1", "x2", True)
list_theta = [(2, 2), (7, 5), (2, 6), (3, 4)]
for theta in list_theta:
    distribution = ot.Dirichlet(theta)
    pdf_curve = distribution.drawPDF()
    cdf_curve = distribution.drawCDF()
    pdf_graph.add(pdf_curve)
    cdf_graph.add(cdf_curve)
legends = [f"theta={theta}" for theta in list_theta]
pdf_graph.setLegends(legends)
cdf_graph.setLegends(legends)
distribution_2d_1 = ot.Dirichlet(theta_1)
distribution_2d_2 = ot.Dirichlet(theta_2)
pdf_2d_1.add(distribution_2d_1.drawPDF())
pdf_2d_2.add(distribution_2d_2.drawPDF())
grid.setGraph(0, 0, pdf_graph)
grid.setGraph(0, 1, cdf_graph)
grid.setGraph(1, 0, pdf_2d_1)
grid.setGraph(1, 1, pdf_2d_2)
grid.setTitle("Dirichlet (theta)")
grid.setLegendPosition("upper right")
v = View(grid)
fig = v.getFigure()
fig.axes[1].legend(loc="best")
