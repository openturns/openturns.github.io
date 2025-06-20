"""
Compute grouped indices for the Ishigami function
=================================================
"""

# %%
#
# In this example, we compute grouped Sobol' indices for the :ref:`Ishigami function <use-case-ishigami>`.

# %%
from openturns.usecases import ishigami_function
import openturns as ot


# %%
# We load the Ishigami test function from usecases module:
im = ishigami_function.IshigamiModel()

# %%
# The `IshigamiModel` data class contains the input distribution of the random vector
# :math:`\vect{X}=\Tr{(X_1, X_2, X_3)}` in `im.inputDistribution` and the Ishigami function in `im.model`.
# We also have access to the input variable names with:
input_names = im.inputDistribution.getDescription()


# %%
# Create a training sample.

# %%
N = 100
inputTrain = im.inputDistribution.getSample(N)
outputTrain = im.model(inputTrain)

# %%
# Create the chaos.

# %%
multivariateBasis = ot.OrthogonalProductPolynomialFactory([im.X1, im.X2, im.X3])
selectionAlgorithm = ot.LeastSquaresMetaModelSelectionFactory()
projectionStrategy = ot.LeastSquaresStrategy(
    inputTrain, outputTrain, selectionAlgorithm
)
totalDegree = 8
enumfunc = multivariateBasis.getEnumerateFunction()
P = enumfunc.getStrataCumulatedCardinal(totalDegree)
adaptiveStrategy = ot.FixedStrategy(multivariateBasis, P)
chaosalgo = ot.FunctionalChaosAlgorithm(
    inputTrain, outputTrain, im.inputDistribution, adaptiveStrategy, projectionStrategy
)

# %%
chaosalgo.run()
result = chaosalgo.getResult()
metamodel = result.getMetaModel()

# %%
# Print Sobol' indices.

# %%
chaosSI = ot.FunctionalChaosSobolIndices(result)
chaosSI

# %%
# We compute the first order indice of the group `[0,1]` .

# %%
chaosSI.getSobolGroupedIndex([0, 1])

# %%
# This group collects all the multi-indices containing variables only in this group, including interactions within the group (by decreasing order of significance):
#
# * [0,4,0] : 0.279938
# * [1,0,0] : 0.190322
# * [0,6,0] : 0.130033
# * [3,0,0] : 0.12058
# * [0,2,0] : 0.0250262

# %%
0.279938 + 0.190322 + 0.130033 + 0.12058 + 0.0250262

# %%
# The difference between the previous sum and the output of `getSobolGroupedIndex` is lower than 0.01, which is the threshold used by the `__str__` method.

# %%
# We compute the total order indice of the group [1,2].

# %%
chaosSI.getSobolGroupedTotalIndex([1, 2])

# %%
# This group collects all the multi-indices containing variables in this group, including interactions with variables outside the group:
#
# * [0,4,0] : 0.279938
# * [1,0,2] : 0.136823
# * [0,6,0] : 0.130033
# * [3,0,2] : 0.0837457
# * [0,2,0] : 0.0250262
# * [1,0,4] : 0.0111867

# %%
0.279938 + 0.136823 + 0.130033 + 0.0837457 + 0.0250262 + 0.0111867
