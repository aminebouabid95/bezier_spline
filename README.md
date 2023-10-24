!! This function is  created by the author, Amine BOUABID, and is based only on mathematical description and not third-party code.
!! This function was developed from scratch and it not optimized in terms of memory and execution time.

Explanation:
bezier_spline(X_points, Y_points, n_steps, show_details) draws a parametric curve using the control points defined by X_points and Y_points.
n, the size of X_points, is the order of the curve. It affects the shape of ther curve between the first and last points.
n = 2 for linear,
n = 3 for quadratic,
n = 4 for cubic,
etc.
X_points and Y_points represent coordinates of the control points of the spline.
The spline will be drawn between the first and the last points defined by their coordinates as (X_points[0], Y_points[0]) and (X_points[-1], Y_points[-1])
n_steps is the number of interpolated points used to draw the spline. By default numpy sets it to 50.
For large values of n_steps (Let's say n_steps > 100), no effect will be visible on the plot.
Contrariwise, for small values of n_steps (Let's say n_steps < 20), the spline will start loosing its smoothness.
show_details plots the control points and the control polygon.
