from math import cos,sin
e = 2.718281828459045235360287471352
running = True
inputa, inputb, inputh = False, False, False

def power(x,y):
    nx = x
    for i in range(1,y):
        nx = nx * x
    if y == 0:
        nx = 1
    return nx

def factorial(x):
    f = 1
    for i in range(1,x+1):
        f = f * i
    return f

def cos_taylor_4digit(x):
    calced_cos = 0 
    i = 0
    counting_cos = True
    while counting_cos:
        new = round(((power(-1,i)) * ((power(x,2*i))/(factorial(2*i)))),4)
        if round(abs(new),4) > 0.0001:
            calced_cos += new
        else:
            counting_cos = False
        i += 1
    return calced_cos
while running:
    
    try:
        if not inputa:
            a = input("Введите a: ")
            if a != 'q':
                a = round(float(a),3)
                inputa = True
            else:
                running = False
    except ValueError:
        print("Not a number, try again!")
        
    try:
        if not inputb and inputa:
            b = (input("Введите b: "))
            if b != 'q':
                b = round(float(b),3)
                inputb = True
            else:
                running = False
    
    except ValueError:
        print("Not a number, try again!")

    try:
        if not inputh and inputa and inputb:
            h = (input("Введите h: "))
            if h != 'q':
                h = round(float(h),3)
                inputh = True
            else:
                running = False
    
    except ValueError:
        print("Not a number, try again!")

    if inputa and inputb and inputh:
        x = a
        while x != round((b + h),3):

            s = 1
            i = 1
            counting = True
            while counting:
                new = cos_taylor_4digit(i*x)/factorial(i)
                if round(abs(new),4) > 0.0001:
                    s += new
                else:
                    print(round(s,4), ((e**(cos(x)))*cos(sin(x))))
                    counting = False
                i += 1
                
            x = round((x + h),3)

        inputa, inputb, inputh = False, False, False
        print('type q to quit!')