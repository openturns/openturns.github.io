import openturns as ot
import openturns.experimental as otexp
from matplotlib import pyplot as plt
from openturns.viewer import View

ot.RandomGenerator.SetSeed(0)
if "AliMikhailHaqCopula" == "EmpiricalBernsteinCopula":
    sample = ot.Dirichlet([1.0, 2.0, 3.0]).getSample(100)
    copula = ot.EmpiricalBernsteinCopula(sample, 4)
elif "AliMikhailHaqCopula" == "ExtremeValueCopula":
    copula = ot.ExtremeValueCopula(ot.SymbolicFunction("t", "t^3/2-t/2+1"))
elif "AliMikhailHaqCopula" == "NormalCopula":
    R = ot.CorrelationMatrix(2)
    R[1, 0] = 0.8
    copula = ot.NormalCopula(R)
elif "AliMikhailHaqCopula" == "SklarCopula":
    student = ot.Student(3.0, [1.0] * 2, [3.0] * 2, ot.CorrelationMatrix(2))
    copula =  ot.SklarCopula(student)
elif "AliMikhailHaqCopula" == "StudentCopula":
    R = ot.CorrelationMatrix(2)
    R[1, 0] = 0.3
    copula = ot.StudentCopula(3.0, R)
else:
    copula = ot.AliMikhailHaqCopula()
if copula.getDimension() == 1:
    copula = ot.AliMikhailHaqCopula(2)
copula.setDescription(["$u_1$", "$u_2$"])
pdf_graph = copula.drawPDF()
cdf_graph = copula.drawCDF()
fig = plt.figure(figsize=(10, 4))
pdf_axis = fig.add_subplot(121)
cdf_axis = fig.add_subplot(122)
View(pdf_graph, figure=fig, axes=[pdf_axis], add_legend=False, square_axes=True)
View(cdf_graph, figure=fig, axes=[cdf_axis], add_legend=False, square_axes=True)
title = str(copula)[:100].split("\n")[0]
fig.suptitle(title)