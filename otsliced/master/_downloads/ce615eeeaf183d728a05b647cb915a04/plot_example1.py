"""
Example on 2-d data
===================
"""

# %%
import openturns as ot
import otsliced

# %%
# Create 2-d data X and 1-d feature Y
N = 100
X = ot.Normal([0.0] * 2, [0.1] * 2).getSample(N)
X += [[-i / (N - 1), 2 * i / (N - 1)] for i in range(N)]
X = X - X.computeMean()
f = ot.SymbolicFunction(["x1", "x2"], ["4*(x1+2*x2)+2"])
Y = f(X) + ot.Normal(0.0, 0.2).getSample(N)

# %%
# Run the SIR algorithm
algo = otsliced.SlicedInverseRegression(X, Y)
transformation = algo.getResult().getTransformation()
