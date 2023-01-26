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