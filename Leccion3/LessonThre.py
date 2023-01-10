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
    number = int(input("Ingrese un numero para validar: "))
    if (number %10) == int((number%100)/10):
        print('El numero ingresado sus dos ultimos digitos son iguales '+ str(number%10))
    else:
        print("El numero ingresado no cumple con la igualda")

""" 
26. Construir un programa que le a un numero entero y detemine si la suma de sus ultimos digitos son iguales.
"""
def SumLatestSeven():
    number = int(input("Ingrese un numero para validar :"))
    if ((number%10)+int((number%100)/10)) == 7:
        print(f'La suma de los dos ultimos digidos dio 7 : {int(number%10)} :: {int((number%100)/10)}')
    else:
        print('El numero ingresado no  cumple con lo solicitado')
"""
27. Construir un programa que lea un numero entero yu determine si el resultado de suimas sus dos ultimos digitos  es un
numero de un 1 digito
"""
def sumBiggerNumber():
    number = int(input("Ingrese un numero para comprobar si sus dos ultimos digitos dan uno solo: "))
    if 1 <= (number%10+int((number%100)/10)) <10:
        print(f'El numero  cumple al ser un solo digito: {str((number%10+int((number%100)/10)))}')
    else: 
        print('El numero no cumple con la condicion')

""" 
28.Construir un programa que lea dos numeros enteros y determine si el 1er numero leido es mayor que el 2 numero leido.
"""
def BiggerNumber():
    numberOne = int(input('Ingrese el primer numero: '))
    numberTwo = int(input('Ingrese el segundo numero: '))
    if numberOne > numberTwo :
        print(f'El primer numero es mayor {numberOne}')
    else: 
        print('El segundo numero no cumple con lo solicitado')

""" 
29. Construir un programa que lea dos numeros enteros y determine si el ultimo digito del 1er numero leido es par
y, al tiempo, si el penultimo digito del 2 nuimero leido es impar
"""
def numbeObbCouple():
    numberOne = int(input('Ingrese el primer numero: '))
    numberTwo = int(input('Ingrese el segundo numero: '))
    if ((numberOne%10)%2 == 0) and int((numberTwo%100)/10)%2 != 0:
        print(f'El primer numero es par: {str(numberOne%10)} segundo numero impar: {str(int((numberTwo%100)/10))}')
    else:
        print('Los numeros no cumplen con lo solicitado')