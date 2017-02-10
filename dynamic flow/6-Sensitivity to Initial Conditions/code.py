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

## plot 2D plots t vs x and t vs y and t vs z
def plot_t_3x(t_axis, x1_axis, x2_axis, x3_axis, x4_axis, x5_axis, x6_axis, label1, label2):
    fig, axarr = plt.subplots(3, sharex=True)
    axarr[0].plot(t_axis, x1_axis, label=label1)
    axarr[0].plot(t_axis, x2_axis, "--", label=label2)
    axarr[0].set_ylabel('$x$', fontsize=18)
    axarr[0].set_xlabel('$t$', fontsize=18)
    axarr[0].legend(loc='upper right')
    axarr[1].plot(t_axis, x3_axis, label=label1)
    axarr[1].plot(t_axis, x4_axis, "--", label=label2)
    axarr[1].set_ylabel('$y$', fontsize=18)
    axarr[1].set_xlabel('$t$', fontsize=18)
    axarr[1].legend(loc='upper right')
    axarr[2].plot(t_axis, x5_axis, label=label1)
    axarr[2].plot(t_axis, x6_axis, "--", label=label2)
    axarr[2].set_ylabel('$z$', fontsize=18)
    axarr[2].set_xlabel('$t$', fontsize=18)
    axarr[2].legend(loc='upper right')
    plt.show()

## plot 2D plot x vs y
def plot_x_y(x_axis, y_axis, x_label, y_label):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    plt.plot(x_axis, y_axis)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    plt.show()
    
## compute the manhattan distance of two points
def distance(x1, y1, z1, x2, y2, z2):
    return abs(x2 - x1) + abs(y2 - y1) + abs(z2 - z1)

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

plt.rcParams.update({'font.size': 10})

## 6. Sensitivity to Initial Conditions

## First part, alpha=beta=0, gamma=1

alpha = 0
betta = 0
gamma = 1
x0 = 0.1
y0 = 0.1
z0 = 0.1
t_max = 300
map1 = dynamic_iter(F, alpha, betta, gamma, x0, y0, z0, t_max)
x0 = 0.001
y0 = 0.001
z0 = 0.001
map2 = dynamic_iter(F, alpha, betta, gamma, x0, y0, z0, t_max)
plot_t_3x(np.arange(t_max), map1[:,0], map2[:,0], map1[:,1], map2[:,1], map1[:,2], map2[:,2], "x0=y0=z0=0.1", "x0=y0=z0=0.001")

## Second part: alpha=0.2, beta = 0.2, gamma = 1.1, x0=y0=z0=0, epsilon = 0.7 

t_max = 1000
alpha = 0.2
betta = 0.2
gamma = 1.1
x0 = 0
y0 = 0
z0 = 0
map1 = dynamic_iter(F, alpha, betta, gamma, x0, y0, z0, t_max)
## if the distance of two points is more than epsilon, 
## we consider it divergence
epsilon = 0.7
iteration = 100
x1 = x0
y1 = y0
z1 = z0
res = np.zeros([iteration, 2])
for i in range(iteration):
    x1 += 0.1
    y1 += 0.1
    z1 += 0.1
    dis = distance(x0, y0, z0, x1, y1, z1)
    map2 = dynamic_iter(F, alpha, betta, gamma, x1, y1, z1, t_max)
    count = 0 ## number of iterations that trajectories are not divergent
    ## count util divergence happens
    for index in range(t_max):
        if distance(map2[index,0], map2[index,1], map2[index,2], x0, y0, z0) > epsilon:
            break
        count += 1
    res[i, 0] = dis
    res[i, 1] = count

## plot the result
plot_x_y(res[:, 0], res[:, 1] , "difference in initial conditions", "number of iterations before divergence")





