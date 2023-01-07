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

""" 
16. Construir un programa que reciba un numero entero y muestr el residuo de divirdilo entre 6 y entre 8.
"""
def remainderofdivision():
    Number = int(input("Ingrese un numero entero para conocer su divicion: "))
    print(f'Resultado de numero dividido en 6: {Number%6} y dividido en 8: {Number%8}')

""" 
17. Construir un programa que reciba dos numeros enteros y muestre el resultado de sumar el ultimo
digito de cada numero.
"""
def addLastDigit():
    NumberOne = int(input("Igrese el primer numero Entero: "))
    NumberTwo = int(input("Ingrese el segundo numero entero: "))
    print(f'Resultado de la suma de los ultimos digitos: {(NumberOne%10)+(NumberTwo%10)}')
""" 
18. Constuir un programa que reciba dos numeros y muestre la suma de sus tres ultimos digitos 
"""
def sumThreDigit():
    Number = int(input("Ingrese el numero para saber la suma de 3 ultimos digitos: "))
    Result = int((Number%1000)/100) + int((Number%100)/10) + int(Number%10)
    print(f'Resultado de la suma de los 3 digitos: {Result}')

""" 
19. Constuir un programa que reciba dos cadenas y determine si las dos cadenas son exactamente iguales
"""
def chainEquals():
    chainOne = str(input("Ingrese primera cadena ha comparar: "))
    chainTwo = str(input("Ingrese segunda cadena ha comparar: "))
    Result =  chainOne == chainTwo
    print(f'El resultado sera a nivel booleado de acuerdo a la comparacion : {Result}')

""" 
20. Construir un programa que reciba dos numeros complejos y muestre la suma de dichos numeros. 
"""

def sumComplex():
    NumberOne = complex(input("Ingrese primer numero complejo: "))
    NumberTwo = complex(input("Ingrese segundo numero complejo: "))
    print(f'Resultado de la suma de numeros complejos: {NumberOne + NumberTwo }')