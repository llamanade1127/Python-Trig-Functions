import math

def FindSASArea(a, b, C):
    return 0.5 * a * b * sinInDeg(C)

def FindASAArea(a, B, C):
    A = 180 - (B + C)
    return 0.5 * pow(a, 2) * ((sinInDeg(B) * sinInDeg(C) / sinInDeg(A)))

def FindSSSArea(a,b,c):
    s = (a + b + c) / 2
    return math.sqrt(s(s-a)(s-b)(s-c))

def sinInDeg(a):
    return math.sin(math.radians(a))

def FindArea(triType):
    match triType:
        case 1:
            area = FindSASArea(float(input('What is side a?\n')),float(input('What is side b?\n')), float(input('What is angle C?\n')))
            print("The area is {}".format(area))
        case 2:
            area = FindASAArea(float(input('What is side a?\n')),float(input('What is angle B?\n')), float(input('What is angle C?\n')))
            print("The area is {}".format(area))
        case 3:
            area = FindSSSArea(float(input('What is side a?\n')),float(input('What is side b?\n')), float(input('What is side c?\n')))
            print("The area is {}".format(area))
        case _:
            return print('Invalid option!')

if __name__ == "__main__":
    print("""
    Thank you for using this!
    This only works with SAS, ASA, and SSS triangles
    Note:
        1. All inputs must be in degrees
        2. Angles must be inputted correctly 
            ex: for SAS, inputing side a, side b, and angle C is correct,
            but inputting side a, side b, angle A is incorrect
        
    """)
    FindArea(int(input("What kind of triangle is it.\n    1.SAS\n    2.ASA\n    3.SSS\n")))
