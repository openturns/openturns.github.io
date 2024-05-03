from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import openturns as ot

x = ot.Normal(3).getSample(1000)
for i in range(len(x)):
    x[i] /= x[i].norm()
xs, ys, zs = map(lambda j: x.getMarginal(j).asPoint(), range(x.getDimension()))

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(xs, ys, zs, marker='.')