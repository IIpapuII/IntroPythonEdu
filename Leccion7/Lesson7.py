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
    phrase = input("Enter string: ")
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
def count_letter_a():
    sentence = input('Enter Sentence: ')
    count = 0
    try: 
        for i in str(sentence.lower()):
            if i in 'a':
                count = count + 1
        print('Number letter  a ', count)
    except:
        print('Bug found')

""" 
70. Construir un programa que permita leer una cadena y mostrar cuantas veces contiene una letra digitada por el usuario
"""
def search_user_letter():
    sentence = input('Enter Sentence: ')
    user_letter = input('Enter letter a search ')
    count = 0
    try:
        for i in str(sentence.lower()):
            if i in str(user_letter.lower()):
                count  = count + 1
        print('Count letter: ', count)
    except:
        print('Bug found')

""" 
71. Construir un programa que permita leer un numero y mostrar el resultado  de dividirlo entre 4.

"""
def number_devisor():
    number = int(input('Enter number: '))
    try:
        print('Result of dividing: ', number/4)
    except ZeroDivisionError as error:
        print('Bug found', error)
""" 

72.  Constuir un programa que permita leer dos numeros enteros y determinar si tienen la misma cantidad de digitos. 
"""
def equal_number_of_lengths():
    numer_one = int(input('Enter number one: '))
    number_two = int(input('Enter numer two: '))

    try:
        if len(str(numer_one)) == len(str(number_two)):
            print('the tow numbers are equal in length')
        else:
            print('Different numbers')
    except:
        print('Different numbers ')