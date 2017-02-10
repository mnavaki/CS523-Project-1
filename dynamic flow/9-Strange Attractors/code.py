## How to run:
## First part: python code.py


import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math
import sys


def F(x, y, z, alpha, betta, gamma):
    xd = x*y - x*gamma + alpha
    yd = -z - x
    zd = betta*z + y
    return [xd, yd, zd]

## set labels for the plot
def init_plot():
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_xlabel(r'$\gamma$', fontsize=24)
    ax.set_ylabel('$x$', fontsize=24)

## it iterates and computes the next points
## it returns the result in arr
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

def plot_xyz(x_axis, y_axis, z_axis, label1, label2, label3):

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x_axis, y_axis, z_axis, color='blue', s=0.5)
    ax.set_xlabel(label1, fontsize=24)
    ax.set_ylabel(label2, fontsize=24)
    ax.set_zlabel(label3, fontsize=24)
    plt.show()

## 9. Strange attractor
plt.rcParams.update({'font.size': 16})

### strange attractor 1: t_max = 100000, alpha = 0.0001, betta = 0.0001, gamma = 1.1, x0 = 0.5,y0 = 0.5,z0 = 0.5
t_max = 100000
alpha = 0.0001
betta = 0.0001
gamma = 1.1

x0 = 0.5
y0 = 0.5
z0 = 0.5
map1 = dynamic_iter(F, alpha, betta, gamma, x0, y0, z0, t_max)
plot_xyz(map1[:,0], map1[:,1], map1[:,2], "x", "y", "z")

### strange attractor 2: t_max = 100000, alpha = 0.0001, betta = -0.0001, gamma = 1.1, x0 = 0.6, y0 = 0.6, z0 = 0.1
t_max = 100000
alpha = 0.0001
betta = -0.0001
gamma = 1.1

x0 = 0.6
y0 = 0.6
z0 = 0.1
map1 = dynamic_iter(F, alpha, betta, gamma, x0, y0, z0, t_max)
plot_xyz(map1[:,0], map1[:,1], map1[:,2], "x", "y", "z")

 

