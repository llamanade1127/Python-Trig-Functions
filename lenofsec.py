import math

def LengthOfSector(radius, angle):
    return 0.5 * pow(radius, 2) * math.radians(angle)


r=float(input("Please enter the radius:"))
a=float(input("Please enter the angle in degrees:"))

print("Length of arc is", LengthOfSector(r, a))

