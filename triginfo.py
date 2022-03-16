import math

def TrigFunctions():
    return """
Trig Functions:
sin = opp/hyp
cos = adj/hyp
tan = opp/adj
csc = 1/sin or hyp/opp
sec = 1/cos or hyp/adj
cot = 1/tan or adj/hyp
    """

def AreaOfTriangle():
    return """
Area of Triangle:
Area = (1/2)a*b*sin(C)      (SAS)
Area = (1/2)a^2 * ((sin(B) * sin(C)) / sin(A))  (ASA)
Area = sqrt(s(s-a)(s-b)(s-c))   (SSS)
    Note: s = (a + b + c) / 2 (semi-perimiter)
    """
def Radians():
    return """
6-1: Radians:
1 radian = 180/pi
1 degree = pi/180
Lenfth of arc: S = rΘ (Θ must he in radians)
Sector of a circle: A = (1/2)r^2*Θ
Segment of circle: (1/2)r^2(Θ - sinΘ)
    """

def GraphingTrig():
    return """
6-4: Graphing Trigs:
Base equation: y = a(kΘ + c) + h
A = Amplitide (Highest value)
    To find amplitude: |a|
    Note: No amplitude for tan or cot
K = period (Length of cycle when graph repeats)
    To find period: (2pi / k) or (360 / k)
    For tan and cot: (pi / k) or (180 / k)
C = Phase Shift (How far left or right it moved)
    To find Phase Shift = (-c / k)
V = Vertical Shift (How far up or down)
    Vertical shift = h
    """

def TrigInverses():
    return """
6-8: Trig inverses:
Sin^-1(1/2) is called a principle value
Sinx => -π/2 <= x <= π/2 (quad I or IV)
Cosx => 0 <= x <= π      (quad I or II)
Tanx => -π/2 < x < π/2   (quad I or IV)
    """

def UnitCircle():
    return """
Unit circle:
0 deg, 0 rad, (1, 0)
30 deg,  π/6, (sqrt(3)/ 2, 1/2) 
45 deg,  π/4, (sqrt(2)/2, sqrt(2)/2)
60 deg,  π/3, (1/2, sqrt(3)/2)
90 deg   π/2, (0, 1)

    """

def PrintInfo(info):
    for i, v in enumerate(info):
        if v == '1':
            print(TrigFunctions())
        elif v == '2':
            print(AreaOfTriangle())
        elif v == '3':
            print(Radians())
        elif v == '4':
            print(GraphingTrig())
        elif v == '5':
            print(UnitCircle())
        elif v == '6':
            print(TrigFunctions())
            print(AreaOfTriangle())
            print(Radians())
            print(GraphingTrig())
            
            

def main():
    print("""
    Thank you for using this!
    Note:
        1. Enter the number of the info you want to print
        2. You can select multiple items
            Ex: If you want both Trig functions and Radians, enter 13
    """)

    PrintInfo(input("""
    0. All info
    1. Trig TrigFunctions
    2. Area of Triangle
    3. 6-1 radians
    4. Graphing Trig Functions
    5. Unit circle
    """))



main()