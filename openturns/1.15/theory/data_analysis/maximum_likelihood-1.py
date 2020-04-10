import openturns as ot
from matplotlib import pyplot as plt
from openturns.viewer import View

distribution = ot.Normal(4.0, 1.0)
graph = distribution.drawPDF()

fig = plt.figure(figsize=(6, 4))
axis = fig.add_subplot(111)
axis.set_xlim(auto=True)

N=6
# coordinates of points
x = [v[0] for v in distribution.getSample(N)]
y = [distribution.computePDF([v]) for v in x]

# draw lines
for dot_x, dot_y in zip(x, y):
    plt.plot([dot_x, 1.0], [dot_y, dot_y], 'b--', linewidth=1.5)
    plt.plot([dot_x, dot_x], [0.0, dot_y], 'b--', linewidth=1.5)

# draw labels
for i in range(N):
    plt.text(x[i]-0.1, -0.015, 'x'+str(i+1))
    plt.text(0.0, y[i]-0.01, 'f_X(x'+str(i+1)+')')

View(graph, figure=fig, axes=[axis], add_legend=True)