
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
#Primera forma de resolver
def reverse_chain_type1(a):
    converText = a.swapcase()
    print(f'Converción: {converText}')

#Segunda forma
def reverse_chain_type2(a):
    wordl = ""
    for i in range(0,len(a)):
        if a[i].islower() == True:
            wordl = f'{wordl}{a[i].upper()}'
        else:
            wordl= f'{wordl}{a[i].lower()}'
    print(f'Retorno de nueva frase: {wordl}')


""" 
5. Construir un programa que lea una cadena  y convierta su contenido en minúsculas.
"""
def convert_to_lowercase(a):
    print(a.lower())
    return a.lower()

""" 
6. Construir un programa que lea una cadena  y convierta su contenido en mayúsculas.
"""
def convert_to_uppercase(a):
    print(a.upper())
    return a.upper()
""" 
7. Construir  un programa que lea una cadena  y la muestre con su 1er carácter  convertido
a mayúscula  y el resto a minúscula.
"""
def convert_firt_capital_letter(a):
    world = a[0].upper()
    print(f'Retorno de la nueva frase: {world}{a[1:].lower()}')



""" 
8. construir un programa que centre una cadena léida en 60 espacios en blanco
"""
def convert_center_chain(a):
    print(a.center(60," "))

""" 
9. Construir un programa que cuente cuántas veces está una subcadena en una cadena, ambas léidas.
"""
def count_subchains(a,b):
    pass

"""
10. Construir un programa que determine si una subcadena está dentro de una cadena, ambas léidas.
"""
def within_substring(a,b):
    if (b in a) == True :
        print(f'{b} esta dentro de {a}')
    else:
        print("No se encontro considencia")

""" 
11. Construir un pograma que muestre en pantalla a partir de dónde se encuentra una subcadena dentro de una cadena
, ambas leídas
"""
def substring_index(a,b):
    print(f'El valor de inicio de la subcadena se encuentra {a.find(b)}')

substring_index(a,b)
""" 
12. Construir un programa que lea una cadena y determine si está compuesta sólo por caracteres alfabéticos, por 
números y letras, sólo números, sólo minúsculas, sólo mayúsculas o sólo espacios en blanco.
"""
def identify_data_type(a):
    pass
