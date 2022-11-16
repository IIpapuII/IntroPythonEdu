"""
11. Constuir un programa que reciba dos números enteros y calcule el resultado de elevar el 1 número
leído por la potencia representada por el 2 número leído.
"""
def Potencia():
    NumberOne = int(input('Ingrese el primer numero para elevar: '))
    NumberTwo = int(input('Ingrese el número para potenciar el primero: '))
    Result =  NumberOne**NumberTwo 
    print('Resultado: '+ str(Result))