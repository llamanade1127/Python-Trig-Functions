import math

def FindIndex(trigType,equation):


 
    #indexes
    indexOfStart = equation.index('(')
    indexOfEnd= equation.index(')')
    
    #split equations y = A(kx + c) + h
    inPer = equation[indexOfStart+1:indexOfEnd]
    after = equation[indexOfEnd+1:]
    before = equation[:indexOfStart]

    #Get indexes for inside
    insideX = inPer.index('X')
    afterX = inPer[insideX+1:]

    k = float(inPer[:insideX]) if inPer.index('X') != 0 else 1
    c = float(afterX) if afterX != '' else 0

    #Get outsides
    a = float(before) if before != '' else 1
    h = float(after) if after != '' else 0

    amplitude = abs(a)
    periodType = 360 if trigType != 't' else 180
    period = (periodType / k)
    phaseShift = -c / k
    verticalShift = h

    def equation(x):
        if trigType == 's':
            return a * math.sin(k*math.radians(x) + math.radians(c)) + h
        elif trigType == 'c':
            return a * math.cos(k*math.radians(x) + math.radians(c)) + h
        elif trigType == 't':
            return a * math.tan(k*math.radians(x) + math.radians(c)) + h

    #trigType
    trigString = 'sin' if trigType == "s" else 'cos' if trigType == 'c' else 'tan' if trigType == 't' else 'NONE'
    equationWithTan = "{}{}({}){}".format(before, trigString, inPer, after)
    print("""
Here are the results
Trig Type: {}
Amplitude: {},
Period: {},
Phase Shift: {},
Vertical Shift: {},
Equation: {},
Base Equation: y = A{}(kx + c) + h
NOTE: ALL ANSERS ARE IN DEGREES
        """.format(trigType, amplitude if trigType != 't' else 'No amplitude for tangent', period if k != 1 else '360',phaseShift if c != 1 else 'None',verticalShift,equationWithTan,trigString ))
    table = input("Do you want table values for this? (y or n)")
    if table == "y":
        print("Table for values between -360 to 360 every 15 degrees")
        for x in range(-360, 360, 15):
            print("{}: {}".format(x, round(equation(x),4)))





print("""

Thank you for using this!
Please note:
1. All inputs must be in degrees
2. No fractions. Ex: 1/2 is 0.5
3. Do not put trig type in equation. Ex 3sin(2x + 4) should be put in as 3(2x+4)
4. No spaces. Ex: 3(2x+4)+4 is good, 3(2x + 4) + 4 is bad
5. Base equation is y = Atrig(kx + c) + h
    """)

FindIndex(input("Please enter the trig type: (s)in, (c)os (t)an: \n"),input("Please enter the equation \n y = "), )

    
