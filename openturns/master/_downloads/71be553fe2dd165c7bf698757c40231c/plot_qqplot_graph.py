"""
Draw the QQ-Plot
================
"""

# %%
# In this example we are going to perform a visual goodness-of-fit test for an 1-d distribution with the QQ plot.

# %%
import openturns as ot
import openturns.viewer as viewer


# %%
# Create data
distribution = ot.Gumbel(0.2, 0.5)
sample = distribution.getSample(100)
sample.setDescription(["Sample"])

# %%
# Fit a distribution
distribution = ot.GumbelFactory().build(sample)

# %%
# Draw QQ plot
graph = ot.VisualTest.DrawQQplot(sample, distribution)
view = viewer.View(graph)

# %%
# Incorrect proposition
graph = ot.VisualTest.DrawQQplot(sample, ot.WeibullMin())
view = viewer.View(graph)

# %%
viewer.View.ShowAll()
