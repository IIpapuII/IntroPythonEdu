""" 
21. Construir un programa que lea un número entero y determine si es número positivo de 4 
"""
def NumerPositiveFour():
    number = int(input("Ingrese un numero :"))
    if number >= 1000 and number<= 9999 :
        print("El numero es positivo y de 4 digitos")
    else:
        print('El numero ingresado no cumple con solicitado')

""" 
22. Construir un programa que lea un numero entero y determine si es numero impar
"""
def oddNumber():
    number = int(input("Ingrese un numero: "))
    if number%2 != 0:
        print(f'El numero ingresado es impar: {number}')
    else:
        print('El numero no cumple la condicion')

""" 
23.Construir un programa que lea un numero entero y determine si es un numero par
"""
def evenNumber():
    number = int(input("Ingrese un numero: "))
    if number%2 == 0:
        print(f'El numero ingresado es par: {number}')
    else:
        print('El numero no cumple la condicion')

""" 
24. Construir un programa que lea un numero entero y determine si su ultimo digito es un digito impar.
"""
def lastOddDigit():
    number = int(input("Ingrese un numero: "))
    if (number%10)%2 != 0:
        print(f'El ultimo digito es impar : {number%10}')
    else:
        print('El ultimo digito no cumple la condicion')

""" 
25. construir un programa que lea un numero entero y determine si sus dos ultimos digitos iguales. 

"""
def numberSame():
    pass