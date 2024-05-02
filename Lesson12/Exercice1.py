
a = input("Ingrese una cadena: ")
b = input("Ingrese una subcadena: ")
def valide_initial_sudstring(a,b):
    """ 
1.Construir un programa que lea una cadena y una subcadena y determine si la cadena
empieza con los caracteres de la subcadena
"""
    if a.startswith(b) == True:
        print( f'PResenta una sudcadena de {b}')
    else:
        print("No inicia con la subcadena")
        


def valide_end_sudstring(a,b):
    """ 
2. Construir un programa que lea una cadena y nuna subcadena y determine si la cadena
finaliza  con los caracteres de la subcadena
"""
    if a.endswith(b):
        print(f'Presenta {b} la sudcadena final')
    else:
        print(f'No se presenta una sudcadena')

#valide_end_sudstring(a,b)

def replace_substring(a,b):
    """ 
3. Construir un programa que lea  una cadena  y, dentro de ella, reemplace
una subcadena por otra (Tambien leidas)
"""
    if b in a :
        c = input("ingrese la cadena a remplazar: ")
        d = a.replace(b,c)
        print(f'Nueva cadena : {d}')
    else:
        print(f'Sudcadena no puede ser remplazada no existe {b}')

""" 
4. Construir un programa que lea una cadena que contiene mayúsculas y  minúsculas  y que
muestre una cadena con las mayúsculas convertidas en minusculas y las minúculas convertidas en
mayúsculas .
"""
def reverse_chain_type(a,b):
    pass

""" 
5. Construir un programa que lea una cadena  y convierta su contenido en minúsculas.
"""
def convert_to_lowercase(a):
    pass

""" 
6. Construir un programa que lea una cadena  y convierta su contenido en mayúsculas.
"""
def convert_to_uppercase(a):
    pass
""" 
7. Construir  un programa que lea una cadena  y la muestre con su 1er carácter  convertido
a mayúscula  y el resto a minúscula.
"""
def convert_firt_capital_letter(a):
    pass



