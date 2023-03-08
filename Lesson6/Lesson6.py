# Desrrollo de la leccion 6 generadores

'''
55. Construir un programa que muestre los numeros multiplos de 4 comprendidos en el rango de 1 y un tope dado.

'''


def number_multiples(a):
    for i in range(a):
        if i % 4 == 0:
            yield i
        else:
            continue


'''
56. Constuir un programa que  muestre los numeros terminados en 3 comprendidos entre 1  y un
tope dado.
'''


def number_printer_stop(a):
    number
    for i in range(a):
        if i % 10 == 3:
            number = yield i
    for i in number:
        print(number)


'''
57. Construir un programa que muestre los numeros cuyos  dos ultimos digitos sumen 4,
en el rango comprendidos entre 1 un numero dado
'''


def sum_four_limit(a):
    numero = 0
    for i in range(a):
        if i%10 + int((i%100)/10) == 4:
            numero = yield i
    return numero

'''
58. Constuir un programa que muestre los numeros cuyos dos ultimos digitos sean iguales,
en el rango comprendido entre 1 y un numero dado.
'''


def equal_number_end(a):
    numero = 0
    for i in range(a):
        if i%10 == int((i%100)/10):
            numero = yield i
    return numero


'''
59. Constuir un programa que muestre los numeros cuyos 3 ultimos digitos sumen 8
en el rago comprendido entre 1 y un numero dado.
'''


def sum_eight_limit(a):
    number = 0
    for i in range(a):
        if i%10 + int((i%100)/10) + int((i%1000)/100) == 8:
            number = yield i
    return number


'''
60. Construir un progrma que muestre los numeros de 2 digitos impares comprendidos en el 
rango comprendido entre 1 y un numero dado.
'''


def print_number_odd(a):
    number = 0
    for i in range(a):
        if len(str(i))== 2 and i%2 ==0:
            number = yield i
    return number


'''
61. Constuir un programa que muentre los numero cuyos 2 ultimos digitos sean multiplos
en el rango comprendido entre 1 y un numero dado.
'''

#Plante el ejercicio de otra forma pero tambies exlui las validaciones con ZeroDivicionError
def print_number_multiples(a):
    number = 0
    for i in range(1,a):
        if len(str(i))>2 and (i%100) != 0:
            if  i % (i%100) == 0:
                number = yield i
    return number

'''
62. Construir un programa que muestre los numeros que comiencen por un digito escrito por el 
usuario en el rango comprendido entre 1 y un numero dado.
'''


def number_range_principle(a:int, b:int):
    number = 0
    for i in range(1,a):
        data = str(i)
        if int(data[0]) == b:
            number = yield i
    return number


'''
63. Cosntruir unn programa que muestre los numeros cuyo primero digito y su ultimo
digito sean iguales, en el rango comprendido entre 1 y un numero dado.
'''


def print_number_range(a):
    number = 0
    for i in range(a):
        data = str(i)
        if i%10 == int(data[0]):
            number = yield i
    return number


'''
64. Constuir un programa que muestre los numeros cuyo primer digito sea multiplo del ultimo
digito, en el rango comprendido entre 1 y un numero dado.
'''


def range_number_principle_multiple(a):
    number = 0
    for i in range(a):
        data = str(i)
        if i%10 != 0 and int(data[0]) != 0:
            if (int(data[0]) % (i%10)) == 0:
               number =  yield i
        else:
            continue
    return number
