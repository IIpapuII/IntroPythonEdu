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


def equal_number_end():
    pass


'''
59. Constuir un programa que muestre los numeros cuyos 3 ultimos digitos sumen 8
en el rago comprendido entre 1 y un numero dado.
'''


def sum_eight_limit():
    pass


'''
60. Construir un progrma que muestre los numeros de 2 digitos impares comprendidos en el 
rango comprendido entre 1 y un numero dado.
'''


def print_number_odd():
    pass


'''
61. Constuir un programa que muentre los numero cuyos 2 ultimos digitos sean multiplos
en el rango comprendido entre 1 y un numero dado.
'''


def print_number_multiples():
    pass


'''
62. Construir un progrma que muestre los numeros que comiencen por un digito escrito por el 
usuario en el rango comprendido entre 1 y un numero dado.
'''


def number_range_principle():
    pass


'''
63. Cosntruir unn programa que muestre los numeros cuyo primero digito y su ultimo
digito sean iguales, en el rango comprendido entre 1 y un numero dado.
'''


def print_number_range():
    pass


'''
64. Constuir un programa que muestre los numeros cuyo primer digito sea multiplo del ultimo
digito, en el rango comprendido entre 1 y un numero dado.
'''


def range_number_principle_multiple():
    pass
