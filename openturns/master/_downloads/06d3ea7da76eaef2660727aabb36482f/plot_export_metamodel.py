"""
Export a metamodel
------------------
"""

# %%
# In this example we will see how to export a metamodel from the context it is created
# to another context where it will actually be used with the help of the pickle module.

# %%
import openturns as ot
from openturns.usecases import cantilever_beam
import pickle

# %%
# Load the cantilever beam use-case.
# We want to use the independent distribution to get meaningful Sobol' indices.
beam = cantilever_beam.CantileverBeam()
g = beam.model
distribution = beam.independentDistribution

# %%
# Generate a learning sample with Monte-Carlo simulation (or retrieve the design from experimental data).
N = 30  # size of the experimental design
X = distribution.getSample(N)
Y = g(X)

# %%
# Build a chaos metamodel
algo = ot.FunctionalChaosAlgorithm(X, Y, distribution)
algo.run()
metamodel = algo.getResult().getMetaModel()

# %%
# Save the metamodel into a `.pkl` file for later use
with open("metamodel.pkl", "wb") as f:
    pickle.dump(metamodel, f)

# %%
# Reload the metamodel in another context from the same `.pkl`
with open("metamodel.pkl", "rb") as f:
    metamodel = pickle.load(f)

# %%
# Reuse the loaded metamodel
x = [6.70455e10, 300.0, 2.55, 1.45385e-07]
y = metamodel(x)
print(y)
