"""
Create an aggregated function
=============================
"""

# %%
# In this example we are going to build a function that stacks all the outputs from several functions
#
# .. math::
#    f = (f_1, \dots, f_n)
#

# %%
import openturns as ot


# %%
# assume a list of functions to aggregate
functions = list()
functions.append(ot.SymbolicFunction(["x1", "x2", "x3"], ["x1^2 + x2", "x1 + x2 + x3"]))
functions.append(
    ot.SymbolicFunction(["x1", "x2", "x3"], ["x1 + 2 * x2 + x3", "x1 + x2 - x3"])
)

# %%
# create the aggregated function
function = ot.AggregatedFunction(functions)

# %%
# evaluate the function
x = [1.0, 2.0, 3.0]
y = function(x)
print("x=", x, "y=", y)
