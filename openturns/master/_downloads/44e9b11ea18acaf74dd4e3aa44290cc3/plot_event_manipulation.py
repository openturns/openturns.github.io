"""
Simulate an Event
=================
"""

# %%
# In this example we are going to define an Event from a scalar variable :math:`Y` in the form:
#
# .. math::
#    Y > T
#
# with :math:`T` a scalar threshold
#

# %%
import openturns as ot


# %%
# Create model f(x) = x1 + 2*x2
model = ot.SymbolicFunction(["x1", "x2"], ["x1+2*x2"])

# Create the input distribution and random vector X
inputDist = ot.Normal(2)
inputDist.setDescription(["X1", "X2"])

inputVector = ot.RandomVector(inputDist)

# Create the output random vector Y=f(X)
outputVector = ot.CompositeRandomVector(model, inputVector)

# %%
# Create the event Y > 3
threshold = 3.0
event = ot.ThresholdEvent(outputVector, ot.Greater(), threshold)

# %%
# Realization as a Bernoulli
print("realization=", event.getRealization())

# %%
# Sample of 10 realizations as a Bernoulli
print("sample=", event.getSample(10))

# %%
# Build a standard event based on an event
standardEvent = ot.StandardEvent(event)
