
.. DO NOT EDIT.
.. THIS FILE WAS AUTOMATICALLY GENERATED BY SPHINX-GALLERY.
.. TO MAKE CHANGES, EDIT THE SOURCE PYTHON FILE:
.. "auto_examples/plot_crosscut_distribution_3d.py"
.. LINE NUMBERS ARE GIVEN BELOW.

.. only:: html

    .. note::
        :class: sphx-glr-download-link-note

        :ref:`Go to the end <sphx_glr_download_auto_examples_plot_crosscut_distribution_3d.py>`
        to download the full example code.

.. rst-class:: sphx-glr-example-title

.. _sphx_glr_auto_examples_plot_crosscut_distribution_3d.py:


Cross-cuts of conditional distributions in 3-d
==============================================

.. GENERATED FROM PYTHON SOURCE LINES 7-8

Conditioning is a way to reduce the dimensionnality of a multivariate distribution. It allows to plot the d

.. GENERATED FROM PYTHON SOURCE LINES 10-14

.. code-block:: Python

    import openturns as ot
    import otbenchmark as otb
    import matplotlib.pyplot as plt








.. GENERATED FROM PYTHON SOURCE LINES 15-17

.. code-block:: Python

    distribution = ot.Normal(3)








.. GENERATED FROM PYTHON SOURCE LINES 18-20

.. code-block:: Python

    referencePoint = distribution.getMean()








.. GENERATED FROM PYTHON SOURCE LINES 21-23

Print the iso-values of the distribution
----------------------------------------

.. GENERATED FROM PYTHON SOURCE LINES 25-28

.. code-block:: Python

    inputDimension = distribution.getDimension()
    description = distribution.getDescription()








.. GENERATED FROM PYTHON SOURCE LINES 29-39

.. code-block:: Python

    crossCut = otb.CrossCutDistribution(distribution)
    fig = crossCut.drawConditionalPDF(referencePoint)
    # Remove the legend labels because there
    # are too many for such a small figure
    for ax in fig.axes:
        ax.legend("")
    # Increase space between sub-figures so that
    # there are no overlap
    plt.subplots_adjust(hspace=0.4, wspace=0.4)




.. image-sg:: /auto_examples/images/sphx_glr_plot_crosscut_distribution_3d_001.png
   :alt: Iso-values of conditional PDF
   :srcset: /auto_examples/images/sphx_glr_plot_crosscut_distribution_3d_001.png
   :class: sphx-glr-single-img


.. rst-class:: sphx-glr-script-out

 .. code-block:: none

    Descr =  1 0
    Descr =  2 0
    Descr =  2 1




.. GENERATED FROM PYTHON SOURCE LINES 40-48

.. code-block:: Python

    fig = crossCut.drawMarginalPDF()
    # Remove the legend labels because there
    # are too many for such a small figure
    for ax in fig.axes:
        ax.legend("")
    # Increase space between sub-figures so that
    # there are no overlap
    plt.subplots_adjust(hspace=0.4, wspace=0.4)



.. image-sg:: /auto_examples/images/sphx_glr_plot_crosscut_distribution_3d_002.png
   :alt: Iso-values of marginal PDF
   :srcset: /auto_examples/images/sphx_glr_plot_crosscut_distribution_3d_002.png
   :class: sphx-glr-single-img






.. rst-class:: sphx-glr-timing

   **Total running time of the script:** (0 minutes 1.341 seconds)


.. _sphx_glr_download_auto_examples_plot_crosscut_distribution_3d.py:

.. only:: html

  .. container:: sphx-glr-footer sphx-glr-footer-example

    .. container:: sphx-glr-download sphx-glr-download-jupyter

      :download:`Download Jupyter notebook: plot_crosscut_distribution_3d.ipynb <plot_crosscut_distribution_3d.ipynb>`

    .. container:: sphx-glr-download sphx-glr-download-python

      :download:`Download Python source code: plot_crosscut_distribution_3d.py <plot_crosscut_distribution_3d.py>`

    .. container:: sphx-glr-download sphx-glr-download-zip

      :download:`Download zipped: plot_crosscut_distribution_3d.zip <plot_crosscut_distribution_3d.zip>`
