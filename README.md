
# CS 523 - Project 1

Group G3

## How to run
To generate all plots use the following commands:

    $chmod +x generate-plots.sh
    $./generate-plots.sh

It prints out what plot currently is showing.

### Dynamical Regimes

    $cd 5-Dynamical\ Regimes
    $python code.py

It draws 3 plots corresponding to fixed point, limit cycle, and complex behaviours respectively.

### Sensitivity to Initial Conditions

    $cd 6-Sensitivity\ to\ Initial\ Conditions
    $python code.py

It draws the plots required for section 6.

### Bifurcations

* First part

        $cd 7-Bifurcations
        $python code.py 0.5 1.4 0.0005

It draws the plot required for the first part of this section. It takes 3 arguments: rho ranges and interval.

* Second part

        $cd 7-Bifurcations
        $python code.py 0.9 1.1 0.0005

It draws the plot required for the second part of this section which is a zoomed version of the plot in the first part.

### Lyapunov Exponent

    $cd 8-Lyapunov\ Exponent
    $python code.py

It plots the Lyaponuv exponent diagram. Also it computes the values of rho and gamma that produces the largest exponent.

### Strange Attractors

    $cd 9-Strange\ Attractors
    $python code.py

It plots the strange attractor in this system.
