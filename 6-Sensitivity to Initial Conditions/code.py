import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math

def F(x, y, rho, gamma):
    xd = rho - x*x + gamma*y
    yd = x
    return [xd, yd]


## plot 2D plots t vs x and t vs y
def plot_t_2x(t_axis, x1_axis, x2_axis, x3_axis, x4_axis, label1, label2):
    fig, axarr = plt.subplots(2, sharex=True)
    axarr[0].plot(t_axis, x1_axis, label=label1)
    axarr[0].plot(t_axis, x2_axis, "--", label=label2)
    axarr[0].set_ylabel('$x$', fontsize=24)
    axarr[0].set_xlabel('$t$', fontsize=24)
    axarr[0].legend(loc='upper right')
    axarr[1].plot(t_axis, x3_axis, label=label1)
    axarr[1].plot(t_axis, x4_axis, "--", label=label2)
    axarr[1].set_ylabel('$y$', fontsize=24)
    axarr[1].set_xlabel('$t$', fontsize=24)
    axarr[1].legend(loc='upper right')
    plt.show()
    

## plot 2D plot x vs y
def plot_x_y(x_axis, y_axis, x_label, y_label):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    plt.plot(x_axis, y_axis)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    plt.show()


## it iterates and computes the next points
## it returns the result in arr
def dynamic_iter(F, rho, gamma, x0, y0, t_max):
    arr = np.zeros([t_max, 2])
    for i in range(t_max):
        [xd, yd] = F(x0, y0, rho, gamma)
        arr[i,0] = xd
        arr[i,1] = yd
        x0 = xd
        y0 = yd
    return arr

## compute the manhattan distance of two points
def distance(x1, y1, x2, y2):
    return abs(x2 - x1) + abs(y2 - y1)


## 6. Sensitivity to Initial Conditions
plt.rcParams.update({'font.size': 16})
## First part

t_max = 200
rho = 1.29
gamma = 0.3
x0 = 0.4
y0 = 0.4
map1 = dynamic_iter(F, rho, gamma, x0, y0, t_max)
x0 = 0.4001
y0 = 0.4
map2 = dynamic_iter(F, rho, gamma, x0, y0, t_max)
## plot the result
plot_t_2x(np.arange(t_max), map1[:,0], map2[:,0], map1[:,1], map2[:,1], "x0 = 0.4, y0=0.4", "x0 = 0.4001, y0=0.4")


## Second part

t_max = 1000
rho = 0.5
gamma = 0.3
x0 = 0
y0 = 0
map1 = dynamic_iter(F, rho, gamma, x0, y0, t_max)
## if the distance of two points is more than epsilon, 
## we consider it divergence
epsilon = 0.05
iteration = 10
x1 = x0
y1 = y0
res = np.zeros([iteration, 2])
for i in range(iteration):
    x1 += 0.1
    y1 += 0.1
    dis = distance(x0, y0, x1, y1)
    map2 = dynamic_iter(F, rho, gamma, x1, y1, t_max)
    count = 0 ## number of iterations that trajectories are not divergent
    ## count util divergence happens
    for index in range(t_max):
        if (abs(map1[index,0] - map2[index,0]) > epsilon):
            break
        count += 1
    res[i, 0] = dis
    res[i, 1] = count

## plot the result
plot_x_y(res[:, 0], res[:, 1] , "difference in initial conditions", "number of iterations before divergence")

