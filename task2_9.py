running = True
inputN, inputP = False, False
while running:
    
    try:
        if not inputN:
            N = input("Введите начальную сумму: ")
            if N != 'q':
                N = int(N)
                inputN = True
            else:
                running = False
    except ValueError:
        print("Not a number, try again!")
        
    try:
        if not inputP and inputN:
            P = (input("Введите процент: "))
            if P != 'q':
                P = int(P)
                inputP = True
            else:
                running = False
    except ValueError:
        print("Not a number, try again!")

    if inputN and inputP:
        N = 1
        c = 0
        while N < 2:
            N = N * (1+(P)/100)
            c += 1
        print(f"Деньги удвоятся за {c} мес.! (Type q to exit)")
        inputN = False
        inputP = False
 
## Ввод изначального кол-ва средств не влияет на время, за которое оно удвоится,
## но раз в задании оно упомянуто, его нужно ввести
    
    