"""
1. Construir un programa que muestre su nombre completo

"""
def FullName():
    Name= 'Wilmer Nemesio Serrano Arias'
    print(Name)

"""
2. Construir un programa que muestre el nombre completo centrado en la ventana de ejecucion. 
"""
def CentrarTexto ():
    Name = 'Wilmer Nemesio Serrano Arias'
    print(Name.center(100, " "))


"""
3. Contruir un programa que almacene dos valores y muestre su suma

"""
def Suma():
    ValorOne = int(input("Ingrese el primer valor a sumar: "))
    ValorTwo = int(input("Ingrese el segundo valor a sumar: "))
    print(ValorOne + ValorTwo)

"""
4. Construir un programa que almacene dos valores y muestre su producto

"""
def Producto():
    ValorOne = int(input("Ingrese el primer a multiplicar: "))
    ValorTwo = int(input("Ingrese el segundo a multiplicar: "))
    print(ValorOne * ValorTwo)

"""
5. Construir un programa que almacene dos valores y muestre el resultado de su resta

"""
def Resta():
    ValorOne = int(input("Ingrese el primero valor a restar: "))
    ValorTwo = int(input("Ingrese el segundo valor a restar: "))
    print(ValorOne - ValorTwo)

"""
6. Constuir un programa que almacene dos valores y muestre el resultado de su divición

"""
def Divicion():
    valorOne = int(input("Ingrese el primer valor a dividir: "))
    ValorTwo = int(input("Ingrese el segundo valor a dividir: "))
    print(valorOne / ValorTwo)

"""
7. Constuir un programa que muestre  la 1  ocurrencia de la cadena "verso" en la palabra "Universo"

"""
def Concidencia():
    PalabraBusqueda = "verso"
    PalabrarABucar = "Universo"
    ConsidenciaEncontrada = PalabrarABucar.find(PalabraBusqueda)
    print(ConsidenciaEncontrada)

"""
8. Contruir un programa que concatene sus nombre con sus apellidos

"""
def concatenar():
    Name = 'Wilmer'
    Surname = 'Serrano'
    Cadena = "Nombre:{0} Apellido: {1}".format(Name, Surname)
    print(Cadena)

"""
9. Construir un programa que escriba su nombre y al frente escriba su edad.
"""
def concatenarEdad():
    Name = 'Wilmer'
    Eage = '21'
    Cadena =  "Nombre: {0} Edad: {1}".format(Name, Eage)
    print(Cadena)

"""
10. Contruir un programa que escriba su nombre, su edad, y su estatura en el mismo renglon utilizando variables
"""
def ConcaTotal():
    Name = "Wilmer"
    Age = "21"
    Height = "1.62 Mts"
    Cadena = "Name: {0} Edad: {1} Estatura: {2}".format(Name,Age,Height)
    print(Cadena)