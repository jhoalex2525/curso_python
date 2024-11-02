# # EJERCICIO CINE
# import math
# ctePi = math.pi
# cilindro = ctePi * (8 / 2) ** 2 * 15
# texto = "El volúmen de empaque con forma"
# texto2 = "te dará más cantidad"
# texto3 = "te dará menor cantidad"
# texto4 = "te dará una cantidad intermedia"
# print(f'{texto} cilíndrica es: {cilindro} cm3')
# rectangular = 12 * 8 * 10
# print(f'{texto} rectangular es: {rectangular} cm3')
# cono = (1 / 3) * ctePi * 6 ** 2 * 12
# print(f'{texto} conica es: {cono} cm3')

# mayorCantidad = max(cilindro, rectangular, cono)
# menorCantidad = min(cilindro, rectangular, cono)

# # MAYOR CANTIDAD
# if mayorCantidad == cilindro:
#     print(f'{texto} cilindrica {texto2}')
# elif mayorCantidad == rectangular:
#     print(f'{texto} rectangular {texto2}')
# elif mayorCantidad == cono:
#     print(f'{texto} conica {texto2}')
# else:
#     print("Vuelve pronto")

# # MENOR CANTIDAD
# if menorCantidad == cilindro:
#     print(f'{texto} cilindrica {texto3}')
# elif menorCantidad == rectangular:
#     print(f'{texto} cilindro {texto3}')
# elif menorCantidad == cono:
#     print(f'{texto} conica {texto3}')
# else:
#     print("Vuelve pronto")

# if cilindro != mayorCantidad and cilindro != menorCantidad:
#     print(f'{texto} cilindrica {texto4}')
# elif rectangular != mayorCantidad and rectangular != menorCantidad:
#     print(f'{texto} rectangular {texto4}')
# else:
#     print(f'{texto} cónica {texto4}')

# # EJERCICIOS
# # 1) vamos a solicitar al usuario ingresar nuestro nombre completo
# # (lo van a ingresar en minuscula)
# nombre_completo = input("Ingresa tu nombre completo: ").lower()
# # - El programa debe imprimir el nombre completamente en mayuscula
# nombre_completo_mayuscula = nombre_completo.upper()
# print(f'Tu nombre en MAYÚSCULAS sería: {nombre_completo_mayuscula}')
# # - El programa debe imprimer el nombre completo pero solo las primeras letras en mayuscula 
# nombre_completo_upper_camel_case = nombre_completo.title()
# print(f'Tu nombre en UpperCamelCase sería: {nombre_completo_upper_camel_case}')

# # 2) crear un programa para ingresar el nombre de un familiar, 
# # (ingresarlo en mayuscula)
# nombre_familiar = input("Ingresa el nombre completo de un familiar: ").upper()
# # -el programa debe imprmir solo la primera letra del texto en mayuscula
# nombre_familiar_primera_letra = nombre_familiar[0].upper()
# print(f'La primera letra del nombre de tu familiar en MAYÚSCULA es: {nombre_familiar_primera_letra}')
# # - imprimir la primera letra de cada palabra en mayuscula
# nombre_familiar_upper_camel_case = nombre_familiar.title()
# print(f'El nombre de tu familiar en UpperCamelCase sería: {nombre_familiar_upper_camel_case}')

# # 3) crear un programa para cambiar la vocales de un texto que ingresa el usuario siguiendo la siguiente estructura:
# # A --> 4
# # E --> 3
# # I --> 1
# # O --> 0
# # el resto de letras seran mayusculas
# texto = input("Ingres un texto: ")
# nuevo_texto = texto.upper().replace('A','4').replace('E','3').replace('I','1').replace('O','0')
# print(f'El nuevo texto sería: {nuevo_texto}')

# TRUE Y FALSE
respuesta = int(input("Ingresar número del 1 al 10: "))
pregunta = respuesta < 5
print("¿El resultado es menor que 5?: ", pregunta)
pregunta = respuesta > 5
print("¿El resultado es mayor que 5?: ", pregunta)
pregunta = respuesta ==5
print("¿El resultado es igual que 5?: ", pregunta)
pregunta = respuesta !=5
print("¿El resultado es diferente que 5?: ", pregunta)

lista_elementos = [0,2,4,6,8]
pregunta = respuesta in lista_elementos
print("¿El resultado está está en lal ista de elementos?: ", pregunta)

pregunta = respuesta is None
print("¿El resultado es nulo?: ", pregunta)

# AND / OR
