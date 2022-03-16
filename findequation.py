def FindEquation(trig, a, pe, ps, vs):
    type =  360 if trig != 't' else 180
    trigString = 'sin' if trig == "s" else 'cos' if trig == 'c' else 'tan' if trig == 't' else 'NONE'
    k = type / pe 
    c = -(k * ps)
    h = vs

    print("""
    a: {}
    k: {}
    c: {}
    h: {}
    Base Equation: y = a(kx + c) + h
    Equation: {}{}({}x + {}) + {}
    
    """.format(a,k,c,h,a,trigString,k,c,h))


print("""
Thank you for using this!
Please note:
1. All inputs must be in degrees
2. No fractions. Ex: 1/2 is 0.5
3. All inputs must be numbers (With the exception of the trig type)
4. Base equation is y = Atrig(kx + c) + h
    """)


FindEquation(input("Please enter the trig type: (s)in, (c)os (t)an: \n"), float(input("Amplitude:")), float(input("Period:")), float(input("Phase Shift:")), float(input("Vertical Shift:")))