
.. DO NOT EDIT.
.. THIS FILE WAS AUTOMATICALLY GENERATED BY SPHINX-GALLERY.
.. TO MAKE CHANGES, EDIT THE SOURCE PYTHON FILE:
.. "auto_examples/reliability_problems/plot_rp8.py"
.. LINE NUMBERS ARE GIVEN BELOW.

.. only:: html

    .. note::
        :class: sphx-glr-download-link-note

        :ref:`Go to the end <sphx_glr_download_auto_examples_reliability_problems_plot_rp8.py>`
        to download the full example code.

.. rst-class:: sphx-glr-example-title

.. _sphx_glr_auto_examples_reliability_problems_plot_rp8.py:


Problem RP8
===========

.. GENERATED FROM PYTHON SOURCE LINES 7-8

In this example, we present the RP8 problem of BBRC 2019 using the FORM SORM method and the Monte Carlo method.

.. GENERATED FROM PYTHON SOURCE LINES 10-13

.. code-block:: Python

    import otbenchmark as otb
    import matplotlib.pyplot as plt








.. GENERATED FROM PYTHON SOURCE LINES 14-17

.. code-block:: Python

    problem = otb.ReliabilityProblem8()
    print(problem)





.. rst-class:: sphx-glr-script-out

 .. code-block:: none

    name = RP8
    event = class=ThresholdEventImplementation antecedent=class=CompositeRandomVector function=class=Function name=Unnamed implementation=class=FunctionImplementation name=Unnamed description=[x1,x2,x3,x4,x5,x6,y0] evaluationImplementation=class=SymbolicEvaluation name=Unnamed inputVariablesNames=[x1,x2,x3,x4,x5,x6] outputVariablesNames=[y0] formulas=[x1 + 2 * x2 + 2 * x3 + x4 - 5 * x5 - 5 * x6] gradientImplementation=class=SymbolicGradient name=Unnamed evaluation=class=SymbolicEvaluation name=Unnamed inputVariablesNames=[x1,x2,x3,x4,x5,x6] outputVariablesNames=[y0] formulas=[x1 + 2 * x2 + 2 * x3 + x4 - 5 * x5 - 5 * x6] hessianImplementation=class=SymbolicHessian name=Unnamed evaluation=class=SymbolicEvaluation name=Unnamed inputVariablesNames=[x1,x2,x3,x4,x5,x6] outputVariablesNames=[y0] formulas=[x1 + 2 * x2 + 2 * x3 + x4 - 5 * x5 - 5 * x6] antecedent=class=UsualRandomVector distribution=class=JointDistribution name=JointDistribution dimension=6 copula=class=IndependentCopula name=IndependentCopula dimension=6 marginal[0]=class=ParametrizedDistribution parameters=class=LogNormalMuSigma name=Unnamed mu=120 sigma=12 gamma=0 distribution=class=LogNormal name=LogNormal dimension=1 muLog=4.78252 sigmaLog=0.0997513 gamma=0 marginal[1]=class=ParametrizedDistribution parameters=class=LogNormalMuSigma name=Unnamed mu=120 sigma=12 gamma=0 distribution=class=LogNormal name=LogNormal dimension=1 muLog=4.78252 sigmaLog=0.0997513 gamma=0 marginal[2]=class=ParametrizedDistribution parameters=class=LogNormalMuSigma name=Unnamed mu=120 sigma=12 gamma=0 distribution=class=LogNormal name=LogNormal dimension=1 muLog=4.78252 sigmaLog=0.0997513 gamma=0 marginal[3]=class=ParametrizedDistribution parameters=class=LogNormalMuSigma name=Unnamed mu=120 sigma=12 gamma=0 distribution=class=LogNormal name=LogNormal dimension=1 muLog=4.78252 sigmaLog=0.0997513 gamma=0 marginal[4]=class=ParametrizedDistribution parameters=class=LogNormalMuSigma name=Unnamed mu=50 sigma=10 gamma=0 distribution=class=LogNormal name=LogNormal dimension=1 muLog=3.89241 sigmaLog=0.198042 gamma=0 marginal[5]=class=ParametrizedDistribution parameters=class=LogNormalMuSigma name=Unnamed mu=40 sigma=8 gamma=0 distribution=class=LogNormal name=LogNormal dimension=1 muLog=3.66927 sigmaLog=0.198042 gamma=0 operator=class=Less name=Unnamed threshold=0
    probability = 0.0007897927545597477





.. GENERATED FROM PYTHON SOURCE LINES 18-21

.. code-block:: Python

    event = problem.getEvent()
    g = event.getFunction()








.. GENERATED FROM PYTHON SOURCE LINES 22-24

Compute the bounds of the domain
--------------------------------

.. GENERATED FROM PYTHON SOURCE LINES 26-29

.. code-block:: Python

    inputVector = event.getAntecedent()
    distribution = inputVector.getDistribution()








.. GENERATED FROM PYTHON SOURCE LINES 30-33

.. code-block:: Python

    inputDimension = distribution.getDimension()
    print(inputDimension)





.. rst-class:: sphx-glr-script-out

 .. code-block:: none

    6




.. GENERATED FROM PYTHON SOURCE LINES 34-39

.. code-block:: Python

    alpha = 1.0 - 1.0e-5
    bounds, marginalProb = distribution.computeMinimumVolumeIntervalWithMarginalProbability(
        alpha
    )








.. GENERATED FROM PYTHON SOURCE LINES 40-43

.. code-block:: Python

    referencePoint = distribution.getMean()
    print(referencePoint)





.. rst-class:: sphx-glr-script-out

 .. code-block:: none

    [120,120,120,120,50,40]




.. GENERATED FROM PYTHON SOURCE LINES 44-54

.. code-block:: Python

    crossCut = otb.CrossCutFunction(g, referencePoint)
    fig = crossCut.draw(bounds)
    # Remove the legend labels because there
    # are too many for such a small figure
    for ax in fig.axes:
        ax.legend("")
    # Increase space between sub-figures so that
    # there are no overlap
    plt.subplots_adjust(hspace=0.5, wspace=0.75)




.. image-sg:: /auto_examples/reliability_problems/images/sphx_glr_plot_rp8_001.png
   :alt: Cross-cuts of function
   :srcset: /auto_examples/reliability_problems/images/sphx_glr_plot_rp8_001.png
   :class: sphx-glr-single-img





.. GENERATED FROM PYTHON SOURCE LINES 55-57

Plot cross-cuts of the distribution
-----------------------------------

.. GENERATED FROM PYTHON SOURCE LINES 59-61

.. code-block:: Python

    crossCut = otb.CrossCutDistribution(distribution)








.. GENERATED FROM PYTHON SOURCE LINES 62-71

.. code-block:: Python

    fig = crossCut.drawMarginalPDF()
    # Remove the legend labels because there
    # are too many for such a small figure
    for ax in fig.axes:
        ax.legend("")
    # Increase space between sub-figures so that
    # there are no overlap
    plt.subplots_adjust(hspace=0.5, wspace=0.75)




.. image-sg:: /auto_examples/reliability_problems/images/sphx_glr_plot_rp8_002.png
   :alt: Iso-values of marginal PDF
   :srcset: /auto_examples/reliability_problems/images/sphx_glr_plot_rp8_002.png
   :class: sphx-glr-single-img





.. GENERATED FROM PYTHON SOURCE LINES 72-74

The correct way to represent cross-cuts of a distribution is to draw the contours
of the PDF of the conditional distribution.

.. GENERATED FROM PYTHON SOURCE LINES 76-85

.. code-block:: Python

    fig = crossCut.drawConditionalPDF(referencePoint)
    # Remove the legend labels because there
    # are too many for such a small figure
    for ax in fig.axes:
        ax.legend("")
    # Increase space between sub-figures so that
    # there are no overlap
    plt.subplots_adjust(hspace=0.5, wspace=0.75)




.. image-sg:: /auto_examples/reliability_problems/images/sphx_glr_plot_rp8_003.png
   :alt: Iso-values of conditional PDF
   :srcset: /auto_examples/reliability_problems/images/sphx_glr_plot_rp8_003.png
   :class: sphx-glr-single-img


.. rst-class:: sphx-glr-script-out

 .. code-block:: none

    Descr =  1 0
    Descr =  2 0
    Descr =  2 1
    Descr =  3 0
    Descr =  3 1
    Descr =  3 2
    Descr =  4 0
    Descr =  4 1
    Descr =  4 2
    Descr =  4 3
    Descr =  5 0
    Descr =  5 1
    Descr =  5 2
    Descr =  5 3
    Descr =  5 4




.. GENERATED FROM PYTHON SOURCE LINES 86-90

.. code-block:: Python

    inputVector = event.getAntecedent()
    event = problem.getEvent()
    g = event.getFunction()








.. GENERATED FROM PYTHON SOURCE LINES 91-93

.. code-block:: Python

    drawEvent = otb.DrawEvent(event)








.. GENERATED FROM PYTHON SOURCE LINES 94-98

.. code-block:: Python

    _ = drawEvent.draw(bounds)
    # Increase space between sub-figures so that
    # there are no overlap
    plt.subplots_adjust(hspace=0.5, wspace=0.75)



.. image-sg:: /auto_examples/reliability_problems/images/sphx_glr_plot_rp8_004.png
   :alt: plot rp8
   :srcset: /auto_examples/reliability_problems/images/sphx_glr_plot_rp8_004.png
   :class: sphx-glr-single-img






.. rst-class:: sphx-glr-timing

   **Total running time of the script:** (0 minutes 7.751 seconds)


.. _sphx_glr_download_auto_examples_reliability_problems_plot_rp8.py:

.. only:: html

  .. container:: sphx-glr-footer sphx-glr-footer-example

    .. container:: sphx-glr-download sphx-glr-download-jupyter

      :download:`Download Jupyter notebook: plot_rp8.ipynb <plot_rp8.ipynb>`

    .. container:: sphx-glr-download sphx-glr-download-python

      :download:`Download Python source code: plot_rp8.py <plot_rp8.py>`

    .. container:: sphx-glr-download sphx-glr-download-zip

      :download:`Download zipped: plot_rp8.zip <plot_rp8.zip>`
