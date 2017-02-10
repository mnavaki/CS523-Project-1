from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import math


## 5. Dynamical Regimes

def F(x, y, rho, gamma):
    xd = rho - x*x + gamma*y
    yd = x
    return [xd, yd]

## plot t vs x,y
def plot_t_xy(t_axis, x_axis, y_axis, label1, label2):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    plt.plot(t_axis, x_axis, linewidth=2, label=label1)
    plt.plot(t_axis, y_axis, linestyle='--', linewidth=3, label=label2)
    ax.set_xlabel('$t$', fontsize=24)
    ax.set_ylabel('$x$,$y$', fontsize=24)
    ax.legend(loc='upper right')
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

## fixed point: rho = 0.4, gamma = 0.2, x0 = 0, y0 = 0
rho = 0.4
gamma = 0.2
x0 = 0
y0 = 0
t_max = 100
arr = dynamic_iter(F, rho, gamma, x0, y0, t_max)
plot_t_xy(np.arange(t_max), arr[:,0], arr[:,1], "x" , "y")

## limit cycle: rho = 0.5, gamma = 0.2, x0 = 0, y0 = 0
rho = 0.5
gamma = 0.2
arr = dynamic_iter(F, rho, gamma, x0, y0, t_max)
plot_t_xy(np.arange(t_max), arr[:,0], arr[:,1], "x" , "y")

## complex: rho = 1.4, gamma = 0.3, x0 = 0, y0 = 0
rho = 1.4
gamma = 0.3
t_max = 6000
arr = dynamic_iter(F, rho, gamma, x0, y0, t_max)
plot_t_xy(np.arange(t_max), arr[:,0], arr[:,1], "x", "y")
## zoomed in plot
plot_t_xy(np.arange(t_max)[5000:5300], arr[5000:5300,0], arr[5000:5300,1], "x", "y")





