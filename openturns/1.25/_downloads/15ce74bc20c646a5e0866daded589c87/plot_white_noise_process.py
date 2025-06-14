"""
Create a white noise process
============================
"""

# %%
# This example details how to create and manipulate a white noise.
# A second order white noise
# :math:`\varepsilon: \Omega \times \mathbb{D} \rightarrow \mathbb{R}^d` is a stochastic
# process of dimension :math:`d` such that the covariance function
# :math:`C(\vect{s},\vect{t})=\delta(\vect{t}-\vect{s})C(\vect{s},\vect{s})`
# where :math:`C(\vect{s},\vect{s})` is the covariance matrix of the process at
# vertex :math:`\vect{s}` and :math:`\delta` the Kroenecker function.
#
# A process :math:`\varepsilon` is a white noise if all finite family of
# locations :math:`(\vect{t}_i)_{i=1, \dots, n} \in \mathbb{D}`,
# :math:`(\varepsilon_{\vect{t}_i})_{i=1, \dots, n}` is independent and
# identically distributed.
#
# The library proposes to model it through the object :class:`~openturns.WhiteNoise` defined
# on a mesh and a distribution with zero mean and finite standard
# deviation.
#
# If the distribution has a mean different from zero, The library writes
# message to prevent the User and does not allow the creation of such a
# white noise.

# %%
import openturns as ot
import openturns.viewer as viewer
from matplotlib import pyplot as plt


# %%
# Define the distribution
sigma = 1.0
dist = ot.Normal(0.0, sigma)

# %%
# Define the mesh
tgrid = ot.RegularGrid(0.0, 1.0, 100)

# %%
# Create the process
process = ot.WhiteNoise(dist, tgrid)
process

# %%
# Draw a realization
realization = process.getRealization()
graph = realization.drawMarginal(0)
graph.setTitle("Realization of a white noise with distribution N(0,1)")
view = viewer.View(graph)

# %%
# Draw a sample
sample = process.getSample(5)
graph = sample.drawMarginal(0)
graph.setTitle(
    str(sample.getSize()) + " realizations of a white noise with distribution N(0,1)"
)
for k in range(sample.getSize()):
    drawable = graph.getDrawable(k)
    drawable.setLegend("realization " + str(k + 1))
    graph.setDrawable(k, drawable)
view = viewer.View(graph)
plt.show()
