from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import math


## 5. Dynamical Regimes

def F(x, y, rho, gamma):
    xd = rho - x*x + gamma*y
    yd = x
    return [xd, yd]

def scatter_x_y(x_axis, y_axis, label1, label2):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_xlabel(label1, fontsize=20)
    ax.set_ylabel(label2, fontsize=20)
    plt.scatter(x_axis, y_axis, color='red', s=1)
    plt.show()

def dynamic_iter(F, rho, gamma, x0, y0, t_max):
    arr = np.zeros([t_max, 2])
    for i in range(t_max):
        [xd, yd] = F(x0, y0, rho, gamma)
        arr[i,0] = xd
        arr[i,1] = yd
        x0 = xd
        y0 = yd
    return arr

plt.rcParams.update({'font.size': 16})

## strange attractor: rho = 1.2, gamma = 0.4, x0=0, y0=0, t_max=100000
rho = 1.2
gamma = 0.4
x0 = 1.1
y0 = 0
t_max = 100000
arr = dynamic_iter(F, rho, gamma, x0, y0, t_max)
scatter_x_y(arr[:,0], arr[:,1], "$x$", "$y$")


