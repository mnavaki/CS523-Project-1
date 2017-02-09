## How to run:
## First part: python code.py 0.5 1.4 0.001
## Second part: python code.py 0.9 1.1 0.001

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math
import sys


def F(x, y, rho, gamma):
    xd = rho - x*x + gamma*y
    yd = x
    return [xd, yd]    

## set labels for the plot
def init_plot():
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_xlabel(r'$\rho$', fontsize=24)
    ax.set_ylabel('$x$', fontsize=24)

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


## 7. Bifurcations x0=-0.1, y0=0.9
plt.rcParams.update({'font.size': 16})

t_max = 400
rho = float(sys.argv[1])
gamma = 0.3

x0 = -0.1
y0 = 0.9
init_plot()
while rho < float(sys.argv[2]):
    map1 = dynamic_iter(F, rho, gamma, x0, y0, t_max)
    rho_arr = np.full((len(map1[:,0]), 1), rho)
    plt.scatter(rho_arr, map1[:,0], color='blue', s=0.5)
    rho += float(sys.argv[3])

plt.show()


