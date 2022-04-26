from formulas import formulas as form


#third layer of input functions
def passiveSingleResistance():
    volt = input("Please enter the gate voltage.")
    amp = input("Please enter the gate current.")
    calc = form.calcPassiveSingleRes(volt,amp)
    print("The resistance of the gate is")
    print(calc)

def passiveSingleVoltage():
    res = input("Please enter the gate resistance.")
    amp = input("Please enter the gate current.")
    calc = form.calcPassiveSingleVol(res,amp)
    print("The voltage of the gate is ")
    print(calc)

def passiveSingleCurrent():
    volt = input("Please enter the gate voltage.")
    res = input("Please enter the gate resistance.")
    calc = form.calcPassiveSingleAmp(volt,res)
    print("The current of the gate is ")
    print(calc)

def passiveDualConductance():
    amp1 = input("Please enter the first gate current.")
    amp2 = input("Please enter the second gate current.")
    vol1 = input("Please enter the first gate voltage.")
    vol2 = input("Please enter the second gate voltage.")
    calc = form.calcPassiveDualCon(amp1,amp2,vol1,vol2)
    print("The resistances of the gate are ")
    print(calc)

def passiveDualResistance():
    amp1 = input("Please enter the first gate current.")
    amp2 = input("Please enter the second gate current.")
    vol1 = input("Please enter the first gate voltage.")
    vol2 = input("Please enter the second gate voltage.")
    calc = form.calcPassiveDualRes(amp1,amp2,vol1,vol2)
    print("The resistances of the gate are ")
    print(calc)

def passiveDualVoltage():
    amp1 = input("Please enter the first gate current.")
    amp2 = input("Please enter the second gate current.")
    z1 = input("Please enter the first gate resistance.")
    z2 = input("Please enter the second gate resistance.")
    z3 = input("Please enter the third gate resistance.")
    z4 = input("Please enter the last gate resistance.")
    calc = form.calcPassiveDualVolt(amp1,amp2,z1,z2,z3,z4)
    print("The voltages of the gate are ")
    print(calc)

def passiveDualCurrent():
    volt1 = input("Please enter the first gate voltage.")
    volt2 = input("Please enter the second gate voltage.")
    z1 = input("Please enter the first gate resistance.")
    z2 = input("Please enter the second gate resistance.")
    z3 = input("Please enter the third gate resistance.")
    z4 = input("Please enter the last gate resistance.")
    calc = form.calcPassiveDualAmp(volt1,volt2,z1,z2,z3,z4)
    print("The currents of the gate are ")
    print(calc)


def activeSingleVolToAmp():
    vol = input("Please enter the gate idle voltage.")
    res = input("Please enter the gate inner resistance.")
    calc = form.calcActiveSingleVolToCurr(vol,res)
    print("The short circuit current of the new gate is ")
    print(calc)

def activeSingleAmpToVol():
    amp = input("Please enter the gate short circuit current.")
    res = input("Please enter the gate inner resistance.")
    calc = form.calcActiveSingleCurrToVol(amp,res)
    print("The idle voltage of the new gate is " )
    print(calc)

# def activeDualVoltage():
#     amp1 = input("Please enter the first gate current.")
#     amp2 = input("Please enter the second gate current.")
#     z1 = input("Please enter the first gate resistance.")
#     z2 = input("Please enter the second gate resistance.")
#     z3 = input("Please enter the third gate resistance.")
#     z4 = input("Please enter the last gate resistance.")
#     calc = form.calcActiveDualVolt(amp1,amp2,z1,z2,z3,z4)
#     print("The voltages of the gate are " )
#     print(calc)

# def activeDualCurrent():
#     volt1 = input("Please enter the first gate voltage.")
#     volt2 = input("Please enter the second gate voltage.")
#     z1 = input("Please enter the first gate resistance.")
#     z2 = input("Please enter the second gate resistance.")
#     z3 = input("Please enter the third gate resistance.")
#     z4 = input("Please enter the last gate resistance.")
#     calc = form.calcActiveDualAmp(volt1,volt2,z1,z2,z3,z4)
#     print("The currents of the gate are " )
#     print(calc)

#second layer of input functions
def passiveSingleGate():
    userInput = input("What values do you want to calculate? r/u/i")
    if userInput == "r":
        passiveSingleResistance()
    elif userInput == "u":
        passiveSingleVoltage()
    elif userInput == "i":
        passiveSingleCurrent()
    else: print("Invalid Input.")

def activeSingleGate():
    userInput = input("What Gate Duality do you want to calculate? vtc/ctv")
    if userInput == "vtc":
        activeSingleVolToAmp()
    elif userInput == "ctv":
        activeSingleAmpToVol()
    else: print("Invalid Input.")

def passiveDualGate():
    userInput = input("What values do you want to calculate? c/r/u/i")
    if userInput == "c":
        passiveDualConductance()
    if userInput == "r":
        passiveDualResistance()
    if userInput == "u":
        passiveDualVoltage()
    if userInput == "i":
        passiveDualCurrent()
    else: print("Invalid Input.")

# def activeDualGate():
#     userInput = input("What values do you want to calculate? u/i")
#     if userInput == "u":
#         activeDualVoltage()
#     if userInput == "i":
#         activeDualCurrent()
#     else: print("Invalid Input.")

#main loop for the calculator, first layer of input functions
while(True):    
    # userInput = input("What gate do you want to calculate? psg/asg/pdg/adg") #single gate
    userInput = input("What gate do you want to calculate? psg/asg/pdg") #single gate
    if userInput == "psg":
        passiveSingleGate()
    elif userInput == "asg":
        activeSingleGate()
    elif userInput == "pdg":
        passiveDualGate()
    # elif userInput == "adg":
    #     activeDualGate()
    else:
        print("Invalid Input.")
