
.. DO NOT EDIT.
.. THIS FILE WAS AUTOMATICALLY GENERATED BY SPHINX-GALLERY.
.. TO MAKE CHANGES, EDIT THE SOURCE PYTHON FILE:
.. "auto_examples/sensitivity_methods/plot_convergence_ishigami.py"
.. LINE NUMBERS ARE GIVEN BELOW.

.. only:: html

    .. note::
        :class: sphx-glr-download-link-note

        :ref:`Go to the end <sphx_glr_download_auto_examples_sensitivity_methods_plot_convergence_ishigami.py>`
        to download the full example code.

.. rst-class:: sphx-glr-example-title

.. _sphx_glr_auto_examples_sensitivity_methods_plot_convergence_ishigami.py:


Convergence of estimators on Ishigami
=====================================

.. GENERATED FROM PYTHON SOURCE LINES 7-14

In this example, we present the convergence of the sensitivity indices of the Ishigami test function.

We compare different estimators.
* Sampling methods with different estimators: Saltelli, Mauntz-Kucherenko, Martinez, Jansen,
* Sampling methods with different design of experiments: Monte-Carlo, LHS, Quasi-Monte-Carlo,
* Polynomial chaos.


.. GENERATED FROM PYTHON SOURCE LINES 16-22

.. code-block:: Python

    import openturns as ot
    import otbenchmark as otb
    import openturns.viewer as otv
    import numpy as np









.. GENERATED FROM PYTHON SOURCE LINES 23-29

When we estimate Sobol' indices, we may encounter the following warning messages:
```
WRN - The estimated first order Sobol index (2) is greater than its total order index...
WRN - The estimated total order Sobol index (2) is lesser than first order index ...
```
Lots of these messages are printed in the current Notebook. This is why we disable them with:

.. GENERATED FROM PYTHON SOURCE LINES 29-32

.. code-block:: Python

    ot.Log.Show(ot.Log.NONE)









.. GENERATED FROM PYTHON SOURCE LINES 33-36

.. code-block:: Python

    problem = otb.IshigamiSensitivity()
    print(problem)





.. rst-class:: sphx-glr-script-out

 .. code-block:: none

    name = Ishigami
    distribution = ComposedDistribution(Uniform(a = -3.14159, b = 3.14159), Uniform(a = -3.14159, b = 3.14159), Uniform(a = -3.14159, b = 3.14159), IndependentCopula(dimension = 3))
    function = ParametricEvaluation([X1,X2,X3,a,b]->[sin(X1) + a * sin(X2)^2 + b * X3^4 * sin(X1)], parameters positions=[3,4], parameters=[a : 7, b : 0.1], input positions=[0,1,2])
    firstOrderIndices = [0.313905,0.442411,0]
    totalOrderIndices = [0.557589,0.442411,0.243684]




.. GENERATED FROM PYTHON SOURCE LINES 37-40

.. code-block:: Python

    distribution = problem.getInputDistribution()
    model = problem.getFunction()








.. GENERATED FROM PYTHON SOURCE LINES 41-42

Exact first and total order

.. GENERATED FROM PYTHON SOURCE LINES 42-47

.. code-block:: Python

    exact_first_order = problem.getFirstOrderIndices()
    print(exact_first_order)
    exact_total_order = problem.getTotalOrderIndices()
    print(exact_total_order)





.. rst-class:: sphx-glr-script-out

 .. code-block:: none

    [0.313905,0.442411,0]
    [0.557589,0.442411,0.243684]




.. GENERATED FROM PYTHON SOURCE LINES 48-50

Perform sensitivity analysis
----------------------------

.. GENERATED FROM PYTHON SOURCE LINES 52-53

Create X/Y data

.. GENERATED FROM PYTHON SOURCE LINES 53-58

.. code-block:: Python

    ot.RandomGenerator.SetSeed(0)
    size = 10000
    inputDesign = ot.SobolIndicesExperiment(distribution, size).generate()
    outputDesign = model(inputDesign)








.. GENERATED FROM PYTHON SOURCE LINES 59-60

Compute first order indices using the Saltelli estimator

.. GENERATED FROM PYTHON SOURCE LINES 60-64

.. code-block:: Python

    sensitivityAnalysis = ot.SaltelliSensitivityAlgorithm(inputDesign, outputDesign, size)
    computed_first_order = sensitivityAnalysis.getFirstOrderIndices()
    computed_total_order = sensitivityAnalysis.getTotalOrderIndices()








.. GENERATED FROM PYTHON SOURCE LINES 65-66

Compare with exact results

.. GENERATED FROM PYTHON SOURCE LINES 66-76

.. code-block:: Python

    print("Sample size : ", size)
    # First order
    # Compute absolute error (the LRE cannot be computed,
    # because S can be zero)
    print("Computed first order = ", computed_first_order)
    print("Exact first order    = ", exact_first_order)
    # Total order
    print("Computed total order = ", computed_total_order)
    print("Exact total order    = ", exact_total_order)





.. rst-class:: sphx-glr-script-out

 .. code-block:: none

    Sample size :  10000
    Computed first order =  [0.302745,0.460846,0.0066916]
    Exact first order    =  [0.313905,0.442411,0]
    Computed total order =  [0.574996,0.427126,0.256689]
    Exact total order    =  [0.557589,0.442411,0.243684]




.. GENERATED FROM PYTHON SOURCE LINES 77-79

.. code-block:: Python

    dimension = distribution.getDimension()








.. GENERATED FROM PYTHON SOURCE LINES 80-81

Compute componentwise absolute error.

.. GENERATED FROM PYTHON SOURCE LINES 81-84

.. code-block:: Python

    first_order_AE = ot.Point(np.abs(exact_first_order - computed_first_order))
    total_order_AE = ot.Point(np.abs(exact_total_order - computed_total_order))








.. GENERATED FROM PYTHON SOURCE LINES 85-91

.. code-block:: Python

    print("Absolute error")
    for i in range(dimension):
        print(
            "AE(S%d) = %.4f, AE(T%d) = %.4f" % (i, first_order_AE[i], i, total_order_AE[i])
        )





.. rst-class:: sphx-glr-script-out

 .. code-block:: none

    Absolute error
    AE(S0) = 0.0112, AE(T0) = 0.0174
    AE(S1) = 0.0184, AE(T1) = 0.0153
    AE(S2) = 0.0067, AE(T2) = 0.0130




.. GENERATED FROM PYTHON SOURCE LINES 92-111

.. code-block:: Python

    metaSAAlgorithm = otb.SensitivityBenchmarkMetaAlgorithm(problem)
    for estimator in ["Saltelli", "Martinez", "Jansen", "MauntzKucherenko", "Janon"]:
        print("Estimator:", estimator)
        benchmark = otb.SensitivityConvergence(
            problem,
            metaSAAlgorithm,
            numberOfRepetitions=4,
            maximum_elapsed_time=2.0,
            sample_size_initial=20,
            estimator=estimator,
        )
        grid = benchmark.plotConvergenceGrid(verbose=False)
        view = otv.View(grid)
        figure = view.getFigure()
        _ = figure.suptitle("%s, %s" % (problem.getName(), estimator))
        figure.set_figwidth(10.0)
        figure.set_figheight(5.0)
        figure.subplots_adjust(wspace=0.4, hspace=0.4)




.. rst-class:: sphx-glr-horizontal


    *

      .. image-sg:: /auto_examples/sensitivity_methods/images/sphx_glr_plot_convergence_ishigami_001.png
         :alt: Ishigami, Saltelli
         :srcset: /auto_examples/sensitivity_methods/images/sphx_glr_plot_convergence_ishigami_001.png
         :class: sphx-glr-multi-img

    *

      .. image-sg:: /auto_examples/sensitivity_methods/images/sphx_glr_plot_convergence_ishigami_002.png
         :alt: Ishigami, Martinez
         :srcset: /auto_examples/sensitivity_methods/images/sphx_glr_plot_convergence_ishigami_002.png
         :class: sphx-glr-multi-img

    *

      .. image-sg:: /auto_examples/sensitivity_methods/images/sphx_glr_plot_convergence_ishigami_003.png
         :alt: Ishigami, Jansen
         :srcset: /auto_examples/sensitivity_methods/images/sphx_glr_plot_convergence_ishigami_003.png
         :class: sphx-glr-multi-img

    *

      .. image-sg:: /auto_examples/sensitivity_methods/images/sphx_glr_plot_convergence_ishigami_004.png
         :alt: Ishigami, MauntzKucherenko
         :srcset: /auto_examples/sensitivity_methods/images/sphx_glr_plot_convergence_ishigami_004.png
         :class: sphx-glr-multi-img

    *

      .. image-sg:: /auto_examples/sensitivity_methods/images/sphx_glr_plot_convergence_ishigami_005.png
         :alt: Ishigami, Janon
         :srcset: /auto_examples/sensitivity_methods/images/sphx_glr_plot_convergence_ishigami_005.png
         :class: sphx-glr-multi-img


.. rst-class:: sphx-glr-script-out

 .. code-block:: none

    Estimator: Saltelli
    Estimator: Martinez
    Estimator: Jansen
    Estimator: MauntzKucherenko
    Estimator: Janon




.. GENERATED FROM PYTHON SOURCE LINES 112-124

.. code-block:: Python

    benchmark = otb.SensitivityConvergence(
        problem,
        metaSAAlgorithm,
        numberOfRepetitions=4,
        maximum_elapsed_time=2.0,
        sample_size_initial=20,
        estimator="Saltelli",
        sampling_method="MonteCarlo",
    )
    graph = benchmark.plotConvergenceCurve()
    _ = otv.View(graph)




.. image-sg:: /auto_examples/sensitivity_methods/images/sphx_glr_plot_convergence_ishigami_006.png
   :alt: Ishigami, Saltelli, MonteCarlo
   :srcset: /auto_examples/sensitivity_methods/images/sphx_glr_plot_convergence_ishigami_006.png
   :class: sphx-glr-single-img





.. GENERATED FROM PYTHON SOURCE LINES 125-153

.. code-block:: Python

    grid = ot.GridLayout(1, 3)
    maximum_absolute_error = 1.0
    minimum_absolute_error = 1.0e-5
    sampling_method_list = ["MonteCarlo", "LHS", "QMC"]
    for sampling_method_index in range(3):
        sampling_method = sampling_method_list[sampling_method_index]
        benchmark = otb.SensitivityConvergence(
            problem,
            metaSAAlgorithm,
            numberOfRepetitions=4,
            maximum_elapsed_time=2.0,
            sample_size_initial=20,
            estimator="Saltelli",
            sampling_method=sampling_method,
        )
        graph = benchmark.plotConvergenceCurve()
        # Change bounding box
        box = graph.getBoundingBox()
        bound = box.getLowerBound()
        bound[1] = minimum_absolute_error
        box.setLowerBound(bound)
        bound = box.getUpperBound()
        bound[1] = maximum_absolute_error
        box.setUpperBound(bound)
        graph.setBoundingBox(box)
        grid.setGraph(0, sampling_method_index, graph)
    _ = otv.View(grid)




.. image-sg:: /auto_examples/sensitivity_methods/images/sphx_glr_plot_convergence_ishigami_007.png
   :alt: , Ishigami, Saltelli, MonteCarlo, Ishigami, Saltelli, LHS, Ishigami, Saltelli, QMC
   :srcset: /auto_examples/sensitivity_methods/images/sphx_glr_plot_convergence_ishigami_007.png
   :class: sphx-glr-single-img





.. GENERATED FROM PYTHON SOURCE LINES 154-155

Use polynomial chaos.

.. GENERATED FROM PYTHON SOURCE LINES 155-170

.. code-block:: Python

    benchmark = otb.SensitivityConvergence(
        problem,
        metaSAAlgorithm,
        numberOfExperiments=12,
        numberOfRepetitions=1,
        maximum_elapsed_time=5.0,
        sample_size_initial=20,
        use_sampling=False,
        total_degree=20,
        hyperbolic_quasinorm=1.0,
    )
    graph = benchmark.plotConvergenceCurve(verbose=True)
    graph.setLegendPosition("bottomleft")
    _ = otv.View(graph)




.. image-sg:: /auto_examples/sensitivity_methods/images/sphx_glr_plot_convergence_ishigami_008.png
   :alt: Ishigami, P.C., Degree=20
   :srcset: /auto_examples/sensitivity_methods/images/sphx_glr_plot_convergence_ishigami_008.png
   :class: sphx-glr-single-img


.. rst-class:: sphx-glr-script-out

 .. code-block:: none

    Elapsed = 0.0 (s), Sample size = 40
    Elapsed = 0.0 (s), Sample size = 80
    Elapsed = 0.1 (s), Sample size = 160
    Elapsed = 0.6 (s), Sample size = 320
    Elapsed = 3.1 (s), Sample size = 640
    Elapsed = 18.45 (s)




.. GENERATED FROM PYTHON SOURCE LINES 171-172

.. code-block:: Python

    otv.View.ShowAll()








.. rst-class:: sphx-glr-timing

   **Total running time of the script:** (0 minutes 46.734 seconds)


.. _sphx_glr_download_auto_examples_sensitivity_methods_plot_convergence_ishigami.py:

.. only:: html

  .. container:: sphx-glr-footer sphx-glr-footer-example

    .. container:: sphx-glr-download sphx-glr-download-jupyter

      :download:`Download Jupyter notebook: plot_convergence_ishigami.ipynb <plot_convergence_ishigami.ipynb>`

    .. container:: sphx-glr-download sphx-glr-download-python

      :download:`Download Python source code: plot_convergence_ishigami.py <plot_convergence_ishigami.py>`

    .. container:: sphx-glr-download sphx-glr-download-zip

      :download:`Download zipped: plot_convergence_ishigami.zip <plot_convergence_ishigami.zip>`
