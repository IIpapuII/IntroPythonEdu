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













