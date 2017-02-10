## How to run:
## First part: python code.py
## Second part: python code.py

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math
import sys
import numpy as NP
from scipy import linalg as LA


def F(x, y, rho, gamma):
    xd = rho - x*x + gamma*y
    yd = x
    return [xd, yd]    

def F_Jacobian(x, gamma):
    mat = np.zeros([2, 2])
    mat[0,0] = -2*x
    mat[0,1] = gamma
    mat[1,0] = 1
    mat[1,1] = 0
    return mat
    
## set labels for the plot
def init_plot():
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_xlabel("rho")
    ax.set_ylabel("x")

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


## 8. Lyapunov Exponent

def lyapunov2d(F, F_Jacobian, t_max, rng, param1, param2, x0, y0):
    current_l= 0;
    max_lyapunovs = np.zeros([len(rng), 1])
    for param1 in rng:
        # Initialize variables
        xy= [x0, y0]
        xy_lengths = [1,0]
        arr = np.zeros([t_max, 1])
        for i in range(t_max):
            J = F_Jacobian(xy[0], param2)
            xy = F(xy[0], xy[1], param1, param2)
            # Calculate divergence rate in the direction defined by the Jacobian
            xy_lengths = np.dot(J, xy_lengths)
            length = np.sqrt( pow(xy_lengths[0], 2) + pow(xy_lengths[1], 2) )
            arr[i] = math.log(length, 2)
        max_lyapunovs[current_l] = np.average(arr) ## Calculate the average
        current_l += 1
    return max_lyapunovs

## first part

max_time= 50
rho = 0.4
gamma = 0.4
# Initial values for x and y
x_attractor = np.sqrt(rho)
y_attractor = 0
x0 = x_attractor
y0 = y_attractor

# Calculate the Lyapunov exponents for first attractor
rng = np.arange(0,1.5,0.001)
Lyapunov_exponents = lyapunov2d(F, F_Jacobian, max_time, rng, gamma, rho, x0, y0)

plt.rcParams.update({'font.size': 16})
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xlabel(r'$\gamma$', fontsize=24)
ax.set_ylabel("Lyapunov exponent", fontsize=18)
ax.axhline(y=0,xmin=0,xmax=3,c="black",linewidth=2,zorder=0)
plt.plot(rng, Lyapunov_exponents)
plt.show()

# Calculate the Lyapunov exponents for second attractor
x_attractor = -1*np.sqrt(rho)
y_attractor = 0
x0 = x_attractor
y0 = y_attractor
Lyapunov_exponents = lyapunov2d(F, F_Jacobian, max_time, rng, gamma, rho, x0, y0)

plt.rcParams.update({'font.size': 16})
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xlabel(r'$\gamma$', fontsize=24)
ax.set_ylabel("Lyapunov exponent", fontsize=18)
ax.axhline(y=0,xmin=0,xmax=3,c="black",linewidth=2,zorder=0)
plt.plot(rng, Lyapunov_exponents)
plt.show()


max_time= 100
rho = 0.4
gamma = 0.3
# Initial values for x and y
x_attractor = np.sqrt(rho)
y_attractor = 0
x0 = 0
y0 = 0

dic = {}
gamma_range =  np.arange(0.1,1.5,0.01)
rho_range = np.arange(0,1.5,0.01)

max_l = np.empty([len(gamma_range)*len(rho_range), 1], dtype=float)
rho_gamma_values = []
i = 0
print "identifying the values of rho and gamma that produces the largest exponent..."
## iterate over gamma
for gamma in gamma_range:

    # Calculate the Lyapunov exponents
    Lyapunov_exponents = lyapunov2d(F, F_Jacobian, max_time, rho_range, rho, gamma, x0, y0)
    l_tmp = Lyapunov_exponents
    l_tmp = l_tmp[~np.isnan(l_tmp)] ## removing nan
    l_tmp = l_tmp[~np.isinf(l_tmp)] ## removing inf
    if len(l_tmp) == 0:
        max_l[i] = -1000
        rho_gamma_values.append("NA")
    else:
        max_l[i] = sorted(list(l_tmp))[-1] ## find max value
        itemindex = np.where(Lyapunov_exponents==max_l[i]) ## find max value's index
        rho_gamma_values.append("rho = " + str(rho_range[itemindex[0]]) + ",gamma =" + str(gamma))
    i += 1

general_max_l = max(max_l)
itemindex = np.where(max_l==general_max_l) ## find max value's index
print "maximum exponent: ", general_max_l
print rho_gamma_values[itemindex[0]]


## Compute eigenvalues
print "Computing eigenvalues..."
gamma = 1
x0=1
y0=1
J = F_Jacobian(x0, gamma)
e_vals, e_vecs = LA.eig(J)
print "eigenvalues: ", e_vals




