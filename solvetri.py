import math

#Returns angle A using law of cosines
def LawOfCosineAngle(a,b,c):
    return math.degrees(math.acos((pow(b, 2) + pow(c, 2) - pow(a,2)) /  (2*b*c)))

#Returns side A using law of cosines
def LawOfCosineSide(A,b,c):
    return math.sqrt(pow(b, 2) + pow(c, 2) - 2 * b * c * math.cos(math.radians(A)))

#Finds B using law of sines
def LawOfSinesAngle(a, A, b):
    return math.degrees(math.asin((b * math.sin(math.radians(A))) / a))

#Finds b using the law of sines
def LawOfSinesSide(a, A, B):
    return (a * math.sin(math.radians(B))) / math.sin(math.radians(A))

def SSSArea(a,b,c):
    s = (a + b + c) / 2
    return math.sqrt(s * (s-a) * (s-b) * (s-c))

def FindUnkAngle(A,B):
    print('180 - ({A} + {B})'.format(A=A,B=B))
    return 180 - (A + B)

def HasTwoSides(A, a ,b):
    return b * math.sin(math.radians(A)) < a < b

#Triangle solves
def SolveAAS(A, B, b):
    print('First find angle C using 180 - (A + B)')
    C = FindUnkAngle(A,B)

    print('Find side a with Law of sines')
    a = LawOfSinesSide(b, B, A)

    print('Find side C using law of sines')
    c = LawOfSinesSide(b, B, C)

    print("Find area using SSS")
    area = SSSArea(a,b,c)

    PrintTriangle(a,A,b,B,c,C,area, 'AAS')

def SolveASA(A,B,c):
    print('Find the unknown angle ')
    C = FindUnkAngle(A,B)

    print('Find the a using the law of sines')
    a = LawOfSinesSide(c, C, A)

    print('Find the b using law of sines')
    b = LawOfSinesSide(c, C, B)

    print("Find area using SSS")
    area = SSSArea(a, b, c)

    PrintTriangle(a,A,b,B,c,C,area,'ASA')

def SolveSAS(A, b, c):
    print("Find a side first using law of sines")
    a = LawOfCosineSide(A, b, c)

    print('To find the next angle, we need to find the smaller angle')
    #Need to find smaller side
    if b < c:
        print('side b is smaller than side c so we find angle B first using law of sines')
        B = LawOfSinesAngle(a, A, b)

        print('Then we find the unknown angle')
        C = FindUnkAngle(A, B)

        print('Find area using SSS')
        area = SSSArea(a, b, c)

        PrintTriangle(a,A,b,B,c,C,area, 'SAS')
    elif c < b:
        print('side c is smaller than side b so we find C using law of sines')
        C = LawOfSinesAngle(a, A, c)

        print('We find the remanding angle')
        B = FindUnkAngle(A, C)

        print('We find area using SSS')
        area = SSSArea(a,b,c)
        PrintTriangle(a,A,b,B,c,C, area, "SAS")
        

##TODO: Triangle can have two possible answers
def SolveSSA(a, A, b):
    print('Find angle B using law of sines')
    B = LawOfSinesAngle(a, A, b)

    print("Find missing angle using 180")
    C = FindUnkAngle(A,B)

    print("Use law of sines to find side c")
    c = LawOfSinesSide(a, A, C)

    print('Find area using SSS')
    area = SSSArea(a,b,c)

    PrintTriangle(a,A,b,B,c,C,area, 'SSA')

    if HasTwoSides(A,a,b):
        print("There are two possible answers for this triangle")
        print('Find other C angle')
        B = 180 - B
        C = FindUnkAngle(B, A)
        c = LawOfSinesSide(a ,A, C)

        area = SSSArea(a,b,c)
        PrintTriangle(a,A,b,B,c,C,area, 'SSA')
    else:
        print("There is only one answer for this triangle")



def SolveSSS(a,b,c):
    print('Find A and B using law of cosines')
    A = LawOfCosineAngle(a,b,c)
    B = LawOfCosineAngle(b,c,a)

    print("Find last angle using 180")
    C = FindUnkAngle(A,B)

    print('Find area using SSS')
    area = SSSArea(a,b,c)

    PrintTriangle(a,A,b,B,c,C,area, 'SSS')


def PrintTriangle(a, A, b, B, c, C, area, type):
    print("""
Triangle info:
Type: {7}
Side a: {0}     Angle A: {1}
Side b: {2}     Angle B: {3}
Side c: {4}     Angle C: {5}

Area: {6}
    """.format(round(a,3), round(A,3), round(b,3), round(B,3), round(c,3), round(C,3),round(area,3)), type)

def main():
    print("""
    Thank you for using this!
    Note:
        1. Enter the number of the info you want to print
        2. You can select multiple items
            Ex: If you want both Trig functions and Radians, enter 13
    """)

    triType = float(input('What is the triangle type?\n1. SSS\n2. SSA\n3. SAS\n4. ASA\n5. AAS\n?'))

    if triType == 1:
        SolveSSS(float(input('What is side a?\n?')),float(input('What is side b?\n?')),float(input('What is side c?\n?')))
    elif triType == 2:
        SolveSSA(float(input('What is side a?\n?')),float(input('What is angle A?\n?')),float(input('What is side b?\n?')))
    elif triType == 3:
        SolveSAS(float(input('What is angle A?\n?')),float(input('What is side b?\n?')),float(input('What is side c?\n?')))
    elif triType == 4:
        SolveASA(float(input('What is angle A?\n?')),float(input('What is angle B?\n?')),float(input('What is side c?\n?')))
    elif triType == 5:
        SolveAAS(float(input('What is angle A?\n:')),float(input('What is angle B?\n:')),float(input('What is side b?\n:')))

main()