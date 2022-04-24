from formulas import formulas as form

def singleGate():
    print("What values do you want to calculate? r/u/i")
    userInput= input
    if userInput == "r":
        calcSingle("resistance")
    if userInput == "u":
        calcSingle("voltage")
    if userInput == "i":
        calcSingle("current")

def dualGate():
    print("What values do you want to calculate? r/u/i")
    userInput= input
    if userInput == "r":
        calcSingle("resistance")
    if userInput == "u":
        calcSingle("voltage")
    if userInput == "i":
        calcSingle("current")

def calcSingle(functionName):
    form

def calcDual(functionName):
    form

print("What gate do you want to calculate? sg/dg") #single gate
userInput = input
if userInput == "sg":
    singleGate()
elif userInput == "dg":
    dualGate()
