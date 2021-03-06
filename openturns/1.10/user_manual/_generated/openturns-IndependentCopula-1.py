import openturns as ot
from matplotlib import pyplot as plt
from openturns.viewer import View
if (ot.IndependentCopula().__class__.__name__=='SklarCopula'):
  myStudent = ot.Student(3.0, [1.0]*2, [3.0]*2, ot.CorrelationMatrix(2))
  copula =  ot.SklarCopula(myStudent)
else:
  copula = ot.IndependentCopula()
if copula.getDimension() == 1:
    copula = ot.IndependentCopula(2)
copula.setDescription(['$u_1$', '$u_2$'])
pdf_graph = copula.drawPDF()
cdf_graph = copula.drawCDF()
fig = plt.figure(figsize=(10, 4))
plt.suptitle(str(copula))
pdf_axis = fig.add_subplot(121)
cdf_axis = fig.add_subplot(122)
View(pdf_graph, figure=fig, axes=[pdf_axis], add_legend=False)
View(cdf_graph, figure=fig, axes=[cdf_axis], add_legend=False)
pdf_axis.set_aspect('equal')
cdf_axis.set_aspect('equal')