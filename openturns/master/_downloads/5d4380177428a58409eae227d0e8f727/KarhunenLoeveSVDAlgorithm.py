import openturns as ot
from matplotlib import pyplot as plt
from openturns.viewer import View

ot.RandomGenerator.SetSeed(0)
mesh = ot.IntervalMesher([128]).build(ot.Interval(-1.0, 1.0))
threshold = 0.001
model = ot.AbsoluteExponential([1.0])
sample = ot.GaussianProcess(model, mesh).getSample(100)
algo = ot.KarhunenLoeveSVDAlgorithm(sample, threshold)
algo.run()
ev = algo.getResult().getEigenvalues()
modes = algo.getResult().getScaledModesAsProcessSample()
g = modes.drawMarginal(0)
g.setXTitle(r"$t$")
g.setYTitle(r"$\sqrt{\lambda_n}\phi_n$")
g.setTitle(r"SVD approx. of KL expansion for $C(s,t)=e^{-|s-t|}$")

fig = plt.figure(figsize=(6, 4))
axis = fig.add_subplot(111)
axis.set_xlim(auto=True)
View(g, figure=fig, axes=[axis], add_legend=False)
