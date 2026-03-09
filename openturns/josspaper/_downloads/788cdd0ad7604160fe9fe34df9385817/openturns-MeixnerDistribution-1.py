import openturns as ot
from matplotlib import pyplot as plt
import openturns.viewer as otv

ot.RandomGenerator.SetSeed(0)
title = None
if "MeixnerDistribution" == "Bernoulli":
    distribution = ot.Bernoulli(0.7)
elif "MeixnerDistribution" == "Binomial":
    distribution = ot.Binomial(5, 0.2)
elif "MeixnerDistribution" == "Hypergeometric":
    distribution = ot.Hypergeometric(10, 4, 7)
elif "MeixnerDistribution" == "CumulativeDistributionNetwork":
    coll = [ot.Normal(2),ot.Dirichlet([0.5, 1.0, 1.5])]
    distribution = ot.CumulativeDistributionNetwork(coll, ot.BipartiteGraph([[0,1], [0,1]]))
elif "MeixnerDistribution" == "Histogram":
    distribution = ot.Histogram([-1.0, 0.5, 1.0, 2.0], [0.45, 0.4, 0.15])
elif "MeixnerDistribution" == "KernelMixture":
    kernel = ot.Uniform()
    sample = ot.Normal().getSample(5)
    bandwidth = [1.0]
    distribution = ot.KernelMixture(kernel, bandwidth, sample)
elif "MeixnerDistribution" == "MaximumDistribution":
    coll = [ot.Uniform(2.5, 3.5), ot.LogUniform(1.0, 1.2), ot.Triangular(2.0, 3.0, 4.0)]
    distribution = ot.MaximumDistribution(coll)
elif "MeixnerDistribution" == "Multinomial":
    distribution = ot.Multinomial(5, [0.2])
elif "MeixnerDistribution" == "RandomMixture":
    coll = [ot.Triangular(0.0, 1.0, 5.0), ot.Uniform(-2.0, 2.0)]
    weights = [0.8, 0.2]
    cst = 3.0
    distribution = ot.RandomMixture(coll, weights, cst)
elif "MeixnerDistribution" == "SmoothedUniform":
    distribution = ot.SmoothedUniform(-1.0, 10.0, 1.0)
elif "MeixnerDistribution" == "TruncatedDistribution":
    distribution = ot.TruncatedDistribution(ot.Normal(2.0, 1.5), 1.0, 4.0)
elif "MeixnerDistribution" == "UserDefined":
    distribution = ot.UserDefined([[1.0], [2.0], [3.0]], [0.4, 0.5, 1.0])
elif "MeixnerDistribution" == "ZipfMandelbrot":
    distribution = ot.ZipfMandelbrot(10, 2.5, 0.3)
elif "MeixnerDistribution" == "Normal":
    cov = ot.CovarianceMatrix([[1.0, -0.5], [-0.5, 1.0]])
    distribution = ot.Normal([0.0, 0.0], cov)
    title = "Normal dist. with correlation coefficient {}".format(cov[0, 1])
else:
    distribution = ot.MeixnerDistribution()

dimension = distribution.getDimension()
if title is None:
    title = str(distribution)[:100].split("\n")[0]
if dimension == 1:
    distribution.setDescription(["$x$"])
    pdf_graph = distribution.drawPDF()
    cdf_graph = distribution.drawCDF()
    fig = plt.figure(figsize=(10, 4))
    pdf_axis = fig.add_subplot(121)
    cdf_axis = fig.add_subplot(122)
    otv.View(pdf_graph, figure=fig, axes=[pdf_axis], add_legend=False)
    otv.View(cdf_graph, figure=fig, axes=[cdf_axis], add_legend=False)
    fig.suptitle(title)
elif dimension == 2:
    grid = ot.GridLayout(1, 2)
    pdf_graph = distribution.drawPDF()
    pdf_contour = pdf_graph.getDrawable(0).getImplementation()
    pdf_contour.setColorBarPosition("")
    pdf_contour.setColorMapNorm("rank")
    pdf_graph.setDrawable(0, pdf_contour)
    cdf_graph = distribution.drawCDF()
    cdf_contour = cdf_graph.getDrawable(0).getImplementation()
    cdf_contour.setColorBarPosition("")
    cdf_contour.setColorMapNorm("rank")
    cdf_graph.setDrawable(0, cdf_contour)
    grid.setGraph(0, 0, pdf_graph)
    grid.setGraph(0, 1, cdf_graph)
    grid.setTitle(title)
    fig = otv.View(grid).getFigure()
    fig.axes[0].set_title("PDF")
    fig.axes[1].set_title("CDF")