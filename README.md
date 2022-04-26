# GateCalculator
### Calculator for electronical gates written with Python NumPy

#### Disclaimer:
Only for Gates which act purely as resistors as of now. Active Gates not implemented properly.

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
Next you have to enter the parameters as asked (r for resistance, i for current and u for voltage)

#### Dual Gate
For Dual Gates only voltage and current can be calculated and you have to enter the resistance matrix for them.
For the multiple parameters of the dual gates you have to enter the values in order of your vector or matrix (so line, after line for the matrix).
The return value is an array with the two result parameters.

