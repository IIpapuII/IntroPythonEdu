""" 
63. Construir un programa que permita leer un numero y calcular la suma de 
sus 3 ultimos digitos
"""
def sum_number_three(number):
    try:
        return number%10 + round((number%100)/10) + round((number%1000)/100)
    except: 
        print("Error encontrado")

""" 
64. Construir un programa que permita leer un numero y mostrar su raiz cuadrada
(para calcular la raiz se calcula  usando math.sqrt) y acontinuacion el valor al cual
se le quiere calcular
"""
import math
def number_sqrt():
    number = int(input("Enter number "))
    try:
        return  math.sqrt(number)
    except:
        print("Error encontrado al ejecutar la raiz")
""" 
65. Construir un programa que permita  leer dos numeros enteros  y calcular  el resultado de elevar
el 1er numero a la potencia representada por el 2 numero

"""
def raising_number():
    number = int(input('Enter Number: '))
    exponent = int (input('Enter Exponent: '))

    try:
        print('Result: ',number**(exponent**2))
    except:
        print('valide Entradas para realizar la operacion matematiaca')

""" 
66. Construir un programa que permita  leer una cadena y mostrar cuantos caracteres tiene.

"""
def chain_string_len():
    chain_string = input("Enter string ")
    try:
        print('len of string ', len(chain_string))
    except:
        print("El valor ingresado es incorrecto para validar")

""" 
67. Construir un programa que permita leer una cadena y  mostrar cuantas palasbras tiene.
"""
def count_string():
    phrase = input("Enter phrase: ")
    count = 0
    #try:
    for i in phrase:
        if i == ' ':
            count = count + 1
    print('Number of wrod: ', count)
    #except:
     #   print("Erro de ingreso de frase")

"""
68. Construir un programa que permita leer  una cadena y mostrar cuantas vocales tiene
"""
def count_vocals():
    phrase = input("Enter string")
    count = 0
    try:
        for i in phrase:
            if i in 'aeiou':
                count = count + 1
        print("Number of Vocalds ", count)
    except:
        print("Error encontrado")

""" 
69. Construir un programa que permita leer una cadena y mostrar cuantas veces contiene la letra A (mayuscula o minuscula)
"""
""" 
70. Construir un programa que permita leer una cadena y mostrar cuantas veces contiene una letra digitada por el usuario
"""
""" 
71. Construir un programa que permita leer un numero y mostrar el resultado  de dividirlo entre 4.

"""
""" 
72.  Constuir un programa que permita leer dos numeros enteros y determinar si tienen la misma cantidad de digitos. 
"""