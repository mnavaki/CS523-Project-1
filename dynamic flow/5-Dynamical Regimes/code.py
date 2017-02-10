from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import math
from mpl_toolkits.mplot3d import Axes3D


## 5. Dynamical Regimes

def F(x, y, z, alpha, betta, gamma):
    xd = x*y - x*gamma + alpha
    yd = -z - x
    zd = betta*z + y
    return [xd, yd, zd]

def plot_t_xyz(t_axis, x_axis, y_axis, z_axis, label1, label2, label3):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    plt.plot(t_axis, x_axis, linewidth=2, label=label1)
    plt.plot(t_axis, y_axis, linestyle='--', linewidth=3, label=label2)
    plt.plot(t_axis, z_axis, linestyle='-.', linewidth=3, label=label3)
    ax.set_xlabel('$t$', fontsize=24)
    ax.set_ylabel('$x$,$y$,$z$', fontsize=24)
    ax.legend(loc='upper right')
    plt.show()

def plot_xyz(x_axis, y_axis, z_axis, label1, label2, label3):

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x_axis, y_axis, z_axis)
    ax.set_xlabel(label1, fontsize=24)
    ax.set_ylabel(label2, fontsize=24)
    ax.set_zlabel(label3, fontsize=24)
    plt.show()

def dynamic_iter(F, alpha, betta, gamma, x0, y0, z0, t_max):
    arr = np.zeros([t_max, 3])
    for i in range(t_max):
        [xd, yd, zd] = F(x0, y0, z0, alpha, betta, gamma)
        arr[i,0] = xd
        arr[i,1] = yd
        arr[i,2] = zd
        x0 = xd
        y0 = yd
        z0 = zd
    return arr

plt.rcParams.update({'font.size': 16})

## fixed point: alpha = 0.8, betta = 0.8, gamma = 1, x0 = 0.2, y0 = 0.2, z0 = 0.2, t_max = 2000
alpha = 0.8
betta = 0.8
gamma = 1
x0 = 0.2
y0 = 0.2
z0 = 0.2
t_max = 2000
arr = dynamic_iter(F, alpha, betta, gamma, x0, y0, z0, t_max)
plot_t_xyz(np.arange(t_max), arr[:,0], arr[:,1], arr[:,2], "x" , "y", "z")
## plot fixed point
plot_xyz(arr[:,0], arr[:,1], arr[:,2], "$x$" , "$y$", "$z$")

## limit cycle: alpha = 0.0001, betta = 0.0001, gamma = 0.7, x0 = 0.2, y0 = 0.2, z0 = 0.2, t_max = 100
alpha = 0.0001
betta = 0.0001
gamma = 0.7
t_max = 100
arr = dynamic_iter(F, alpha, betta, gamma, x0, y0, z0, t_max)
plot_t_xyz(np.arange(t_max), arr[:,0], arr[:,1], arr[:,2], "x" , "y", "z")

## complex: alpha = 0.1, betta = 0.1, gamma = 1.1, x0 = 0.2, y0 = 0.2, z0 = 0.2, t_max = 500
alpha = 0.1
betta = 0.1
gamma = 1.1
t_max = 500
arr = dynamic_iter(F, alpha, betta, gamma, x0, y0, z0, t_max)
plot_t_xyz(np.arange(t_max), arr[:,0], arr[:,1], arr[:,2], "x" , "y", "z")




