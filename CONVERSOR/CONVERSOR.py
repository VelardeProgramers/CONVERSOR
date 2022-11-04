print("Bienvenido al conversor de moneda")
print("1. Pesos Colombianos")
print("2. Pesos Argentinos")
print("3. Pesos Mexicanos")

opcion = int (input(" Ingrese la opcion: "))
if opcion == 1:
    pesos = float (input("Cuantos pesos Colombianos tienes: "))
    ValorDolar = 3875
    Dolares = pesos / ValorDolar
    Dolares = round(Dolares, 2)
    Dolares = str(Dolares)
    print ("Tienes $ "+ Dolares + " dolares")
elif opcion == 2:
    pesos = float (input("Cuantos pesos Argentinos tienes: "))
    ValorDolar = 65
    Dolares = pesos / ValorDolar
    Dolares = round(Dolares, 2)
    Dolares = str(Dolares)
    print ("Tienes $ "+ Dolares + " dolares")
elif opcion == 3:
    pesos = float (input("Cuantos pesos Mexicanos tienes: "))
    ValorDolar = 24
    Dolares = pesos / ValorDolar
    Dolares = round(Dolares, 2)
    Dolares = str(Dolares)
    print ("Tienes $ "+ Dolares + " dolares")
else:
    print ("Ingrese una opcion correcta, por favor")
