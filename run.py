# print('Hola mundo')

# def saluda(nombre):
#     return 'hola {nombre}, bienvenido alcurso de python'.format(nombre=nombre)

# print(saluda('Adriana'))
# print(saluda('Brayan'))
# print(saluda('Jhonatan'))
# print(saluda('Ludy'))

# 26 de Octubre 2024
# nombre = input('Ingresa tu nombre: ')
# print(f'Ingresaste: {nombre}')
# SUMA +
print('9 + 5 = ', 9+5)

# RESTA -
print('12 - 4 = ', 12-4)

# MULTIPLICACIÓN *
print('2 * 3 = ', 2*3)

# DIVISIÓN -
print('16 / 2 = ', 16/2)
print('17 / 2 = ', 17/2)

# Par redondear decimales usamos la función round
print(round(2.8888, 1))

#Módulo, resultado, parte entera resultado, módulo división
print(17%2)
print(3478/26)
print(3478//26)
print(3478%26)

# Potencia y Raíz
print(2 * 2 * 2 * 2 * 2)
print(2**5)
print(2**10)
print(25**(1/2))
print(27**(1/3))
print(32**(1/5))
print(8**(1/2))

# EJERCICIO OPERACIONES
print('sumar 56 a 89: ', 56+89)
print('adicionar 55 a 31: ', 55+31)
print('agregar 11 a 12: ', 11+12)
print('restar 1587 menos 258: ', 1587-258)
print('disminur 111 a 8888: ', 8888-111)
print('quitar 8 a 65: ', 65-8)
print('multiplicar 8 por 53: ', 8*53)
print('dividir 81 en 3: ', 81/3)
print('dividir 95 en 3 (con decimales): ', 95/3)
print('dividir 95 en 3 (sin decimales, es decir solo la parte entera: ', round(95/3,0))
print('el modulo de 95 en 3: ', 95%3)
print('potenciar 5 veces 6: ', 6**5)
print('cual es el cuadrado de 12: ', 12**2)
print('cual es la raiz cuadrada de 121: ', 121**(1/2))
print('raiz cubica de 729: ', 729**(1/3))

# EJERCICIO PIZZA
import math
personas = 6
cte_pi = math.pi
print('Área pizza pequeña: ', cte_pi * (25/2)**2 * 3) 
print('Área pizza mediana: ', cte_pi * (30/2)**2 * 2) 
print('Área pizza grande: ', cte_pi * (45/2)**2 * 1) 

# EJERCICIO NÓMINA
empleados = int(input("¿Cuántos empleados calculará?: "))

for i in range(empleados):
    tipoCalculo = int(input("Para calcular solo por horas escriba 1. Para calcular por horas por semanas escriba 2. Para calcular por horas por días escriba 3. Para salir marque otro número: "))    
    if (tipoCalculo == 1):
        nombre = input("Ingresa nombre empleado: ")
        horas = int(input("Ingresa número de horas laboradas: "))        
        valorHora = int(input("Ingresa valor de 1 hora laborada: "))        
        total = horas * valorHora        
        print(f'{nombre} trabajó {horas} horas, a {valorHora} COP. Por tanto se le paga {total}')    
    elif (tipoCalculo == 2):
        nombre = input("Ingresa nombre empleado: ")
        horas = int(input("Ingresa número de horas laboradas: "))        
        semanas = int(input("Ingresa número de semanas laboradas: "))        
        valorHora = int(input("Ingresa valor de 1 hora laborada: "))
        total = horas * semanas * valorHora
        print(f'{nombre} trabajó {horas} horas a la semana, durante {semanas} semanas, a {valorHora} COP. Por tanto se le paga {total}')        
    elif (tipoCalculo == 3):
        nombre = input("Ingresa nombre empleado: ")
        horas = int(input("Ingresa número de horas laboradas: "))        
        dias = int(input("Ingresa número de dias laborados: "))
        valorHora = int(input("Ingresa valor de 1 hora laborada: "))        
        total = horas * dias * valorHora
        print(f'{nombre} trabajó {horas} horas, durante {dias} días, a {valorHora} COP. Por tanto se le paga {total}')
    else:
        print("Hasta la próxima")