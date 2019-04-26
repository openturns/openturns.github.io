FractionalBrownianMotionModel
==============================================================================

.. plot::
    :include-source: False

    import openturns as ot
    from matplotlib import pyplot as plt
    from openturns.viewer import View
    if ot.FractionalBrownianMotionModel().__class__.__name__ == 'ExponentialModel':
        covarianceModel = ot.ExponentialModel([0.5], [5.0])
    elif ot.FractionalBrownianMotionModel().__class__.__name__ == 'GeneralizedExponential':
        covarianceModel = ot.GeneralizedExponential([2.0], [3.0], 1.5)
    elif ot.FractionalBrownianMotionModel().__class__.__name__ == 'ProductCovarianceModel':
        amplitude = [1.0]
        scale1 = [4.0]
        scale2 = [4.0]
        cov1 = ot.ExponentialModel(scale1, amplitude)
        cov2 = ot.ExponentialModel(scale2, amplitude)
        covarianceModel = ot.ProductCovarianceModel([cov1, cov2])
    elif ot.FractionalBrownianMotionModel().__class__.__name__ == 'RankMCovarianceModel':
        variance = [1.0, 2.0]
        basis = ot.LinearBasisFactory().build()
        covarianceModel = ot.RankMCovarianceModel(variance, basis)
    else:
        covarianceModel = ot.FractionalBrownianMotionModel()
    title = str(covarianceModel)[:100]
    if covarianceModel.getInputDimension() == 1:
        scale = covarianceModel.getScale()[0]
        if covarianceModel.isStationary():
            def f(x):
                return [covarianceModel(x)[0, 0]]
            func = ot.PythonFunction(1, 1, f)
            func.setDescription(['$tau$', '$cov$'])
            cov_graph = func.draw(-3.0 * scale, 3.0 * scale, 129)
            cov_graph.setTitle(title)
            fig = plt.figure(figsize=(10, 4))
            cov_axis = fig.add_subplot(111)
            View(cov_graph, figure=fig, axes=[cov_axis], add_legend=False)
        else:
            def f(x):
                return [covarianceModel([x[0]], [x[1]])[0, 0]]
            func = ot.PythonFunction(2, 1, f)
            func.setDescription(['$s$', '$t$', '$cov$'])
            cov_graph = func.draw([-3.0 * scale]*2, [3.0 * scale]*2, [129]*2)
            cov_graph.setTitle(title)
            fig = plt.figure(figsize=(10, 4))
            cov_axis = fig.add_subplot(111)
            View(cov_graph, figure=fig, axes=[cov_axis], add_legend=False, square_axes=True)
    elif covarianceModel.getInputDimension() == 2:
        scale = covarianceModel.getScale()
        if covarianceModel.isStationary():
            def f(x):
                return [covarianceModel(x)[0, 0]]
            func = ot.PythonFunction(2, 1, f)
            func.setDescription(['$s$', '$t$', '$cov$'])
            cov_graph = func.draw(-3.0 * scale, 3.0 * scale, [129]*2)
            cov_graph.setTitle(title)
            fig = plt.figure(figsize=(10, 4))
            cov_axis = fig.add_subplot(111)
            View(cov_graph, figure=fig, axes=[cov_axis], add_legend=False, square_axes=True)

.. currentmodule:: openturns

.. autoclass:: FractionalBrownianMotionModel

  
   .. automethod:: __init__
   