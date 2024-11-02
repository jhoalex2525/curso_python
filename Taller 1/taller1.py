# 2) Ejercicios Prácticos:
# 2.1 Imprime los días de la semana
print("2.1 Imprime los días de la semana")
print("Lunes")
print("Martes")
print("Miércoles")
print("Jueves")
print("Viernes")
print("Sábado")
print("Domingo")
 
# 2.2 imprime los meses del año
print("2.2 imprime los meses del año")
print("Enero")
print("Febrero")
print("Marzo")
print("Abril")
print("Mayo")
print("Junio")
print("Julio")
print("Agosto")
print("Septiembre")
print("Octubre")
print("Noviembre")
print("Diciembre")

# 3) Crea una calculadora basica en python 
# crea 4 archivos de python que soliciten al usuario cada número para realizar las 
# respectivas operaciones:
# suma.py
# resta.py
# multiplicacion.py
# div.py

# Reto: 

# El interés simple es el dinero extra que se gana o se paga por prestar o invertir
# una cantidad de dinero, calculado solo sobre el monto inicial (o capital).

# Por ejemplo, si prestas $100 a una tasa de interés simple del 5% anual durante 3 años,
# el interés será:
# C * i * t = I
# 100×0.05×3=15

# Así que, al final, recibirías $115 en total ($100 de capital + $15 de interés).

# 1 ) Crear una aplicacion en python que le permita al usuario calcular el total a pagar de una deuda 
# el programa debe solicitar al usuario los montos de: 
# (capital inicial, tasa de interes anual, tiempo en años) 
print("Cálculo del total a pagar de una deuda")
capital = float(input("Igrese el capital: "))
interes = float(input("Igrese la tasa de interés anual en %, es decir si es 5%, ingrese 5 solamente: "))
tiempo = float(input("Igrese el tiempo en años: "))
operacion = capital * ( 1 + ( interes / 100) * tiempo )
print(f'El total a pagar para un capital de {capital}, con un interés de {interes}% anual, a {tiempo} años es: {operacion}')