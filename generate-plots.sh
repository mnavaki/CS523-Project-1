#!/bin/bash

echo "hello, $USER. I wish to list some files of yours"
echo "listing files in the current directory, $PWD"
ls  # list files

echo "plotting figures related to part I ..."
echo "plotting Fig. 1a - 1d: Dynamical Regimes ..."
cd 5-Dynamical\ Regimes
python code.py

echo "plotting Fig. 2a and 2b: Sensitivity to Initial Conditions  ..."
cd ../6-Sensitivity\ to\ Initial\ Conditions
python code.py

echo "plotting Fig. 3a: Bifurcations ..."
cd ../7-Bifurcations
python code.py 0.5 1.4 0.001
echo "plotting Fig. 3b: zoomed in Bifurcations ..."
python code.py 0.9 1.1 0.001

echo "plotting Fig. 4a and 4b: Lyapunov Exponent ..."
cd ../8-Lyapunov\ Exponent
python code.py

echo "plotting Fig. 5: Strange Attractors ..."
cd ../9-Strange\ Attractors
python code.py

# dynamical flow
echo "\n\nplotting figures related to part II ..."

echo "plotting Fig. 1a - 1d: Dynamical Regimes ..."
cd ../dynamic\ flow/5-Dynamical\ Regimes
python code.py

echo "plotting Fig. 2a - 2b: Sensitivity to Initial Conditions ..."
cd ../6-Sensitivity\ to\ Initial\ Conditions
python code.py

echo "plotting Fig. 3- strange attractor ..."
cd ../9-Strange\ Attractors
python code.py


