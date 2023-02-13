# Desarrollo de la quinta lección sobre funciones los ejercicios a desarrollar


""" 
45. Construir una funccion que reciba su nombre como parametro y que lo muestre 5 veces

"""


def print_name(name, amount):
    for i in range(amount):
        print(f'{i} => {name}')


'''
46. Construir una funcion que reciba una cadena digitada (como parametro)
por el usuario y que lo muestre n veces en pantalla, El valor de n tambien digitado por el usuario
'''


def repeat_text(text, amount):
    for i in range(amount):
        print(f'{i} => {text}')


'''
47. Construir  una funcion que reciba (como parametro) una lista de datos numericos y retorne
la suma de dichos numeros.
'''


def sum_of_number(list_numbers):
    print(sum(list_numbers))


'''
48. Constuir una funcion que reciba (como parametro) una lista de datos numericos
y retorne el promedio de los datos pares.
'''


def average_pairs(list_numbers):
    data = [i for i in list_numbers if i % 2 == 0]
    print(round(sum(data) / len(data), 2))


'''
49. Construir una funcion que reciba (como parametro) una lista de datos numericos
y retorne el promedio de dichos datos.
'''


def average_data(list_numbers):
    print(f'promedio => {round(sum(list_numbers)/len(list_numbers),3)}')


'''
50. Construir una funcion que reciba (como parametros) una lista de cadenas
y retorne la suma de la cantidad de letras de cada cadena
'''


def add_string(txt):
    print('Se inoran en la cuenta de la cadena los espacios')
    for i in txt.split(' '):
        print(f'largo del string => {i} => {len(i)}')


'''
51. Construir una funcion que reciba dos datos enteros (como parametros ) 
y retorne el dato mayor
'''


def greater_data(a, b):
    if a > b:
        print(f'Dato mayor: {a}')
    else:
        print(f'Dato mayor: {b}')


'''
52. Construir una funcion que reciba un valor entero (como parametro)
 y muestre la tabla de multiplicar de dicho valor recibido.
'''


def multiplication_table(a):
    for i in range(1, 11):
        print(f'{i}X{a} => {i*a}')


'''
53. Construir una funcion que reciba un valor entero (como parametro) y determine si su ultimo digito es 4

'''


def last_digit_four(d):
    if d % 10 == 4:
        print(f'Dato con 4 al final: {d}')
    else:
        print('El dato no cumple la condicion')


'''
54. Construir una funcion que reciba una lista de datos enteros (como parametro) y
retorne la cantidad de valores de la lista que terminan en 4.
'''


def last_digit_list(a):
    print([i for i in a if i % 10 == 4])
