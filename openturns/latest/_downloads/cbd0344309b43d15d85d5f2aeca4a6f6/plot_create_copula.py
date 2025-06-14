"""
Create a copula
===============
"""

# %%
# In this example we are going to create a Normal copula from a correlation matrix.
#

# %%
import openturns as ot


# %%
# Create the distribution
R = ot.CorrelationMatrix(3)
R[0, 1] = 0.25
R[1, 2] = 0.25
copula = ot.NormalCopula(R)
print(copula)
