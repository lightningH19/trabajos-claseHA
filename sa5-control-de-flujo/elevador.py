while 1 >0:
    base = float(input("Introduzca la base (el número a elevar) puede ser decimal: "))
    pot = float(input("Introduzca la potencia: "))
    pot =  round(pot, 0)
    print(f"{base} ^ {pot} = {base ** pot}")