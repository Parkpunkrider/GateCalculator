# GateCalculator
### Calculator for electronical gates written with Python NumPy

#### Disclaimer:
Only for Gates which act purely as resistors as of now (so no phase shift). Active Gates are not implemented properly.

#### How to use it
The calculator works as a CLI based application and is deployed via docker.
Just pull the [image](https://hub.docker.com/r/parkpunkrider/numpy-gate-calculator) from Dockerhub 
by running it with "docker run -it --rm parkpunkrider/numpy-gate-calculator" with elevated rights.
Then type python main.py in the console.
To exit the program press ctrl + c and then type exit to shutdown and delete the docker container.


#### What can it do?
You can calculate different Values for passive and active single gates and passive and active dual gates.
First the cli asks you to choose which kind of gate you want to calculate: 
passive single (psg), active single (asg), passive dual(pdg) or active dual (adg).
Next you have to enter the parameters as asked (c for conductivity, r for resistance, i for current and u for voltage)

#### Dual Gate
For Passive Dual Gates conductivity, resistance, voltage and current can be calculated, you have to enter the resistance matrix for the latter two.
For the multiple parameters of the dual gates you have to enter the values in order of your vector or matrix (so line, after line for the matrix).
The return value is an array with the two result parameters.

