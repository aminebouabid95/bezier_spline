# Author: Amine BOUABID

# Explanation:
# bezier_spline(X_points, Y_points, n_steps, show_details) draws a parametric curve using the control points defined by X_points and Y_points.
# X_points and Y_points represent coordinates of the control points of the spline.
# The spline will be drawn between the first and the last points defined by their coordinates as (X_points[0], Y_points[0]) and (X_points[-1], Y_points[-1])
# n_steps is the number of interpolated points used to draw the spline. By default numpy sets it to 50.
# For large values of n_steps (Let's say n_steps > 100), no effect will be visible on the plot.
# Contrariwise, for small values of n_steps (Let's say n_steps < 20), the spline will start loosing its smoothness.
# show_details plots the control points and the control polygon.

def bezier_spline(X_points, Y_points, n_steps, show_details):
    from math import comb
    from numpy import linspace, zeros, power
    from matplotlib.pyplot import axis, grid, plot, scatter, show

    n=len(X_points)

    t=linspace(0,1,n_steps)
    P=zeros((2,len(t)))
    for k in range(n):
        P=P+[comb(n-1,k)*power(1-t, n-1-k)*power(t,k)*X_points[k], comb(n-1,k)*power(1-t, n-1-k)*power(t,k)*Y_points[k]]

    axis('equal')
    grid('both')
    scatter([X_points[0],X_points[-1]],[Y_points[0],Y_points[-1]])
    plot(P[0],P[1],linewidth=2)
    
    if show_details:
        scatter(X_points,Y_points,color='blue',s=20)
        plot(X_points,Y_points, linewidth=1, color=(0.5,0.5,0.5), linestyle='--')

    show()

# Example (Uncomment to try)
# bezier_spline(X_points=[-1, 3, 5, 10], Y_points=[-2, -5, 3, 5], n_steps=50, show_details=True)