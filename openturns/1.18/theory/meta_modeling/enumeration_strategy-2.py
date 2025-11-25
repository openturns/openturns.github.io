import openturns as ot
from matplotlib import pyplot as plt
from openturns.viewer import View

nrows=3
ncols=4

# coordinates of grid
grid = ot.Box([5, 5], ot.Interval([0.0]*2, [6.0]*2))
sample = grid.generate()
grid_x = sample.getMarginal(0)
grid_y = sample.getMarginal(1)

#plt.rc('text', usetex=True)

q_values = [1.0, 0.75, 0.5]
fig = plt.figure()
index = 1
for i in range(nrows):
    q = q_values[i]
    enumerate = ot.HyperbolicAnisotropicEnumerateFunction(2, q)
    for j in range(ncols):
        ax = fig.add_subplot(nrows, ncols, index, aspect=1.0)
        ax.plot(grid_x, grid_y, 'xr')
        strataIndex = j + 3
        strata_x, strata_y = [], []
        strataCardinal = enumerate.getStrataCumulatedCardinal(strataIndex)
        for ii in range(strataCardinal):
            x = enumerate(ii)
            strata_x.append(x[0])
            strata_y.append(x[1])
        ax.plot(strata_x, strata_y, 'ob')
        ax.set_yticks([])
        #ax.set_title('$||x||_{'+str(q)+'} \leq '+str(strataIndex)+'$')
        ax.set_title('||x||q=' + str(q) + ' < ' + str(strataIndex))
        index += 1
plt.subplots_adjust(hspace=0.5)
plt.show()