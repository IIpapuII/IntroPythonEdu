"""
11. Constuir un programa que reciba dos números enteros y calcule el resultado de elevar el 1 número
leído por la potencia representada por el 2 número leído.
"""
def Potencia():
    NumberOne = int(input('Ingrese el primer numero para elevar: '))
    NumberTwo = int(input('Ingrese el número para potenciar el primero: '))
    Result =  NumberOne**NumberTwo 
    print('Resultado: '+ str(Result))

"""
12. Construir un programa que reciba un número entero y obtenga la mitad entera

"""
def WholeNumber():
    Number = int(input("Ingrese un número para optener su mitad: "))
    Outcome = round(Number/2)
    print(f'La mitad  número entero es: {Outcome}')

"""
  13. Construir un programa que reciba un número entero y que muestre su ultimo dígito.
"""
def LastDigit():
    Numer = int(input("Ingrese un Numero y conoce su ultimo difito: "))
    Outcome = Numer % 10
    print(f'El valor del ultimo digito es: {Outcome}')

"""
14. Construir un programa  que reciba un numero entero y muestre el resultado de sumar
sus dos ultimos digitos

"""

def SumaTwoDigit():
    Number = int(input("Ingrese un Numero y conoce la suma de sus ultimos digitos: "))
    Outcome = int(((Number%100)/10) ) + (Number%10)
    print(f'El valor de la suma es la siguiente : {Outcome}')

"""
15. Construir un  programa que reciba un numero entero y muestre el resultado de 
elevar un penultimo digito a la potencia representada por su ultimo digito.

"""
def PenultimateDigitPower():
    Number = int(input("Ingrese un Numero y conoce la potencia de sus ultimos digitos: "))
    Outcome = int(((Number%100)/10) ) ** (Number%10)
    print(f'El valor de la potencia es la siguiente : {Outcome}')