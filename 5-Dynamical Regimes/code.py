import numpy as np
import matplotlib.pyplot as plt

## 5. Dynamical Regimes

def F(x, y, rho, gamma):
    xd = rho - x*x + gamma*y
    yd = x
    return [xd, yd]

def plot_t_xy(t_axis, x_axis, y_axis):
    plt.plot(t_axis, x_axis)
    plt.plot(t_axis, y_axis, linestyle=':', linewidth=3)
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

x0 = 1
y0 = 1
## fixed point
rho = 0.1
gamma = 0.2
t_max = 100
arr = dynamic_iter(F, rho, gamma, x0, y0, t_max)
plot_t_xy(np.arange(t_max), arr[:,0], arr[:,1])

## limit cycle
rho = 0.5
gamma = 0.2
arr = dynamic_iter(F, rho, gamma, x0, y0, t_max)
plot_t_xy(np.arange(t_max), arr[:,0], arr[:,1])

## complex
t_max = 5000
arr = dynamic_iter(F, rho, gamma, x0, y0, t_max)
plot_t_xy(np.arange(t_max), arr[:,0], arr[:,1])



