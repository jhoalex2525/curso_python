print("Va a calcular la división de A/B")
numero = float(input("Igrese número A: "))
numero1 = float(input("Igrese número B: "))
if numero1 != 0:
    operacion = numero / numero1
    print(f'El resultado de dividir {numero} en {numero1} es: {operacion}')
else:
    print("No es posible dividir por cero 0")