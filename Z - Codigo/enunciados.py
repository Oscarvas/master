# A1
def a1 ():
    monedas = (1,5,25)

    print("Dame la cantidad de dinero que deseas cambiar:")
    dinero = int(input())

    r1 = dinero % monedas[2]
    r2 = dinero % monedas[1]
    r3 = dinero % monedas[0]

    print (r1,r2,r3)
a1()
