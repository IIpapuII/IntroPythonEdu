""" 
30. dek conjunto de datos mostrar  [20,21,30,41,50,51,201] monstrar en pantalla los que terminan en uno

"""
def NumberArrayOne(number):
    for i in number:
        if i%10 != 1:
            print(f'El siguiente valor  no termina en uno: {i}')
   
""" 
31. Mostrar 10 veces la palabra Programacion
"""
def PrinterString():
    i =0
    while i<= 10:
        print("Programacion")

'''32. Del conjunto de cadenas ["E","F","M","A"], que corresponden 
a las iniciales  de los primeros cuatro meses del año, mostrar el nombre  completo
de dichos meses usando sentencia repetitivas y condicionales.
'''
def print_years():
    data = ["E","F","M","A"]
    for i in data:
        if i == "E":
            print("January")
        elif i == "F":
            print("February")
        elif i == "M":
            print("March")
        elif i == "A":
            print("April")
        else:
            print("Value error")

'''
33. Del conjunto de datos ["OMAR",54,2,"LUIS",45,3,"JUAN",39,1]mostrar en pantalla
los datos organizados en tres columnas que tengan por titulo NOMBRE,EDAD e HIJOS.
'''

def print_people_table():
    data = ["OMAR",54,2,"LUIS",45,3,"JUAN",39,1,"Carlos",43,1]
    a=0
    print(f'|------------------------|')
    print(f'| NOMBRE | EDAD | HIJOS  |')
    print(f'¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯')
    for i in range(int(len(data)/3)):
        print(f'|{data[a]}\t |  {data[a+1]}  |   {data[a+2]}    |')
        a=a+1
        a=a+2
    print(f'¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯')


''' 
34. Leer una cadena de caracteres y mostrarla verticalmente.
'''
def vertical_text():
    pass

'''
35. Leer una cadena y derterminar cuantas veces dicha cadena  contiene
la letra A en mayuscula.

'''
def letter_repeater():
    pass

'''
36. contruir un programa en python que calcule la suma de todos los numeros 
comprendidos entre 1 y 1000.

'''
def sum_thousand():
    pass

'''
37. Mostrar los multiplos de 5 comprendidos en 13 y 48

'''
def number_multiples():
    pass

'''
38. Mostrar los numeros entre 10 y 31 avanzando de 6 en.
'''
def advanced_by_six():
    pass

'''
39. Mostrar los nombres completos de los meses y al frente la 
la cantidad  de letras que tiene cada nombre.
'''
def number_months():
    pass

'''
40. Mostrar  los entreos comprendidos entre 1 y 30 exeptuando los
multiplos de 3.
'''
def multiples_of_three():
    pass

'''
41. Mostrar los numeros  pares comprendios en 1  y 20. Al final
mostrar las suma de dichos numeros pares.
'''
def add_pairs():
    pass

'''
42. Leer una frese y derteminar cuantas vocales tiene.
'''
def sum_vowels():
    pass

'''
43. Leer una frese y determinar  cuantas palabras tiene.
'''
def add_words():
    pass

'''
44. Leer una palabra  y determinar  cuantas silabas simples tiene.
'''
def add_syllables():
    pass








