from formulas import formulas as form
import numpy as np

#third layer of input functions
def passiveSingleResistance():
    volt = input("Please enter the gate voltage.")
    amp = input("Please enter the gate current.")
    calc = form.calcPassiveSingleRes(volt,amp)
    print("The resistance of the gate is" + calc)

def passiveDualVoltage():
    volt1 = input("Please enter the first gate voltage.")
    volt2 = input("Please enter the second gate voltage.")
    amp1 = input("Please enter the first gate current.")
    amp2 = input("Please enter the second gate current.")
    calc = form.calcPassiveDualVolt(volt1,volt2,amp1,amp2)
    print("The voltages of the gate are " + calc)

def passiveDualCurrent():
    volt1 = input("Please enter the first gate voltage.")
    volt2 = input("Please enter the second gate voltage.")
    amp1 = input("Please enter the first gate current.")
    amp2 = input("Please enter the second gate current.")
    calc = form.calcPassiveDualAmp(volt1,volt2,amp1,amp2)
    print("The currents of the gate are " + calc)

def activeSingleResistance():
    volt = input("Please enter the gate voltage.")
    amp = input("Please enter the gate current.")
    calc = form.calcActiveSingleRes(volt,amp)
    print("The resistance of the gate is " + calc)

def activeSingleVoltage():
    res = input("Please enter the gate resistance.")
    amp = input("Please enter the gate current.")
    calc = form.calcActiveSingleVol()
    print("The resistance of the gate is " + calc)

def activeSingleCurrent():
    volt = input("Please enter the gate voltage.")
    res = input("Please enter the gate resistance.")
    calc = form.calcActiveSingleAmp(volt,res)
    print("The resistance of the gate is " + calc)

def activeDualVoltage():
    volt1 = input("Please enter the first gate voltage.")
    volt2 = input("Please enter the second gate voltage.")
    amp1 = input("Please enter the first gate current.")
    amp2 = input("Please enter the second gate current.")
    calc = form.ca(volt1,volt2,amp1,amp2)
    print("The voltages of the gate are " + calc)

def activeDualCurrent():
    volt1 = input("Please enter the first gate voltage.")
    volt2 = input("Please enter the second gate voltage.")
    amp1 = input("Please enter the first gate current.")
    amp2 = input("Please enter the second gate current.")
    calc = form.calcPassiveSingle(volt1,volt2,amp1,amp2)
    print("The currents of the gate are " + calc)

#second layer of input functions
def passiveSingleGate():
    userInput = input("What values do you want to calculate? r/u/i")
    if userInput == "r":
        passiveSingleResistance()
    elif userInput == "u":
        passiveSingleResistance()
    elif userInput == "i":
        passiveSingleResistance()
    else:
        "Invalid Input."

def activeSingleGate():
    userInput = input("What values do you want to calculate? r/u/i")
    if userInput == "r":
        activeSingleResistance()
    elif userInput == "u":
        activeSingleResistance()
    elif userInput == "i":
        activeSingleResistance()
    else:
        "Invalid Input."

def passiveDualGate():
    userInput = input("What values do you want to calculate? u/i")
    if userInput == "u":
        passiveDualVoltage("voltage")
    if userInput == "i":
        passiveDualCurrent("current")

def activeDualGate():
    userInput = input("What values do you want to calculate? r/u/i")
    if userInput == "r":
        ac
    if userInput == "u":
        calcSingle("voltage")
    if userInput == "i":
        calcSingle("current")

while(True):    #main loop for the calculator, first layer of input functions
    userInput = input("What gate do you want to calculate? psg/asg/pdg/adg") #single gate
    if userInput == "psg":
        passiveSingleGate()
    elif userInput == "asg":
        activeSingleGate()
    elif userInput == "pdg":
        activeDualGate()
    elif userInput == "adg":
        passiveDualGate()
    else:
        print("Invalid Input.")
