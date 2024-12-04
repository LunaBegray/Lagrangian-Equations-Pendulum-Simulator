import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy.integrate import solve_ivp
from mpl_toolkits.mplot3d import Axes3D

g = 9.81

def plot_animation( t, qx, qy, qz, x, y, z ):
    plotInterval = 1
    fig = plt.figure(figsize=(8,8))
    ax = fig.add_subplot(111, projection='3d')
    ax.view_init(30, 45)
    ax.set_xlim( -1.0, 1.0 )
    ax.set_ylim( -1.0, 1.0 )
    ax.set_aspect('equal')
    
    # Initialize trace arrays to store the pendulum's path
    trace_x = []
    trace_y = []
    trace_z = []
    
    # Plot the initial ring (pendulum's circular path) and the pendulum string
    ax.plot(qx, qy, qz, 'k')  # ring
    a = ax.plot([qx[0], x[0]], [qy[0], y[0]], [qz[0], z[0]], 'g')  # pendulum string
    b = ax.plot([x[0]], [y[0]], [z[0]], 'ro')  # pendulum bob
    
    def animate(i):
        # Add the current position to the trace
        trace_x.append(x[i])
        trace_y.append(y[i])
        trace_z.append(z[i])
        
        # Plot the trace (path) of the pendulum
        ax.plot(trace_x, trace_y, trace_z, 'b', alpha=0.5)  # Trace in blue with transparency

        # Update the string and pendulum bob positions
        a[0].set_data_3d([qx[i], x[i]], [qy[i], y[i]], [qz[i], z[i]])
        b[0].set_data_3d([x[i]], [y[i]], [z[i]])
        
    ani = animation.FuncAnimation(fig, animate, interval=4, frames=len(t))
    plt.show()

def plot_figure(qx, qy, qz, x, y, z):
    fig = plt.figure(figsize=(8,8))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(qx, qy, qz, 'k')  # disk
    ax.plot(x, y, z, 'b')  # bob trajectory
    ax.plot((qx[-1], x[-1]), (qy[-1], y[-1]), (qz[-1], z[-1]), 'g')  # final line
    ax.plot(x[-1], y[-1], z[-1], 'ro')  # final bob
    ax.view_init(30, 45)
    ax.set_xlim(-1.0, 1.0)
    ax.set_ylim(-1.0, 1.0)
    ax.set_aspect('equal')
    plt.show()

def deriv(t, Y, R, omega, L):
    x, y, z, xdot, ydot, zdot = Y
    qx, qy = R * math.cos(omega * t), R * math.sin(omega * t)
    qxdot, qydot = -omega * R * math.sin(omega * t), omega * R * math.cos(omega * t)
    twoLambda = (g * z + (R ** 2 - qx * x - qy * y) * omega ** 2 - (xdot - qxdot) ** 2 - (ydot - qydot) ** 2 - zdot ** 2) / L ** 2
    xddot = twoLambda * (x - qx)
    yddot = twoLambda * (y - qy)
    zddot = twoLambda * z - g
    return [xdot, ydot, zdot, xddot, yddot, zddot]

R = 0.5
omega = 2.0
L = 1.0

Y0 = [R, 0.0, -L, 0.0, 0.0, 0.0]
period = 2 * np.pi / omega
tmax = 5 * period
solution = solve_ivp(deriv, [0, tmax], Y0, args=(R, omega, L), rtol=1.0e-6, dense_output=True)

t = np.linspace(0, tmax, 1000)
Y = solution.sol(t)
x = Y[0, :]
y = Y[1, :]
z = Y[2, :]

# Position on disk
qx = R * np.cos(omega * t)
qy = R * np.sin(omega * t)
qz = np.zeros_like(qx)

#plot_figure(qx, qy, qz, x, y, z)
plot_animation(t, qx, qy, qz, x, y, z)
