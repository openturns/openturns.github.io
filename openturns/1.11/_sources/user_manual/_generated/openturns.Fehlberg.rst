Fehlberg
==================

.. plot::
    :include-source: False

    import openturns as ot
    from matplotlib import pyplot as plt
    from openturns.viewer import View

    def flow(X):
        Y0 = X[0]
        Y1 = X[1]
        dY0 = Y0 * (2.0 - Y1)
        dY1 = Y1 * (Y0 - 1.0)
        return [dY0, dY1]

    phi_func = ot.PythonFunction(2, 2, flow)
    phi = ot.ValueFunction(phi_func)
    solver = ot.Fehlberg(phi)

    initialState = [2.0, 2.0]
    nt = 47
    dt = 0.1
    timeGrid = ot.RegularGrid(0.0, dt, nt)
    result = solver.solve(initialState, timeGrid)
    xMin = result.getMin()
    xMax = result.getMax()
    delta = 0.2 * (xMax - xMin)
    mesh = ot.IntervalMesher([12]*2).build(ot.Interval(xMin - delta, xMax + delta))
    field = ot.Field(mesh, phi_func(mesh.getVertices()))
    ot.ResourceMap.SetAsScalar("Field-ArrowScaling", 0.1)
    graph = field.draw()
    cloud = ot.Cloud(mesh.getVertices())
    cloud.setColor("black")
    graph.add(cloud)
    curve = ot.Curve(result)
    curve.setColor("red")
    curve.setLineWidth(2)
    graph.add(curve)

    fig = plt.figure()
    ax = fig.add_subplot(111)
    View(graph, figure=fig)
    plt.suptitle("Lotka-Volterra ODE system")
    plt.xlabel(r'$y_0$')
    plt.ylabel(r'$y_1$')
    plt.grid()

.. currentmodule:: openturns

.. autoclass:: Fehlberg

   
   .. automethod:: __init__
   