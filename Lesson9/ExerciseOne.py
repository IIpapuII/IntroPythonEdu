
""" 
Una veterinaria atiende solmamente perros y los registra en una base  de datos.
Se requiere un programa que lea la información básica del perro 
(no más de 8 características) y se muestra en pantalla. En esta veterinaria
todos los animales  que llegan, entran con el estado inicial de  NO ATENDIDO
 y cuando se registran se cambia automáticamente a ATENDIDO.
Por ahora como la veterinaria solo atiende perros, basado en el peso
(menos de 10kg o mas de 10kg) los registra como "Perro Grande" o "Perro pequeño".

"""


class Vet:
    def __init__(self, name, breed, age, owerName, birthDate, color, weight):
        self.Name: str = name
        self.breed: str = breed
        self.age: int = age
        self.icomeStatus: bool = False
        self.owerName: str = owerName
        self.birthDate: str = birthDate
        self.color: str = color
        self.weight: int = weight
        self.sizeDog: str = "Perro Pequeño" if weight < 10 else "Perro Grande"
        

    def statusIcome(self):
        self.icomeStatus = True

    def enterDog():
        Name = input("Ingrese el nombre del perro: ")
        breed = input("Ingrese la raza del perro: ")
        age = int(input("Ingrese los años del perro: "))
        owerName = input("Ingrese el nombre del dueño: ")
        birthDate = input("Ingrese la Fecha de cumpleaños del perro: ")
        color = input("Ingrese el color del perro: ")
        weight = int(input("Ingrese el peso del perro: "))
        return Name,breed, age, owerName, birthDate, color, weight

def vetMain():
    print("############################### VETERINARIA PYTHON #########################################")
    dogs =[]
    while True:
        choise = int(input("""¿Desea registrar un nuevo perro? 
                           1-SI 
                           2-NO
                           3-lISTAR REGISTROS 
                           : """))
        if choise == 2:
            break
        if choise == 1:
            dog = Vet(*Vet.enterDog())
            dog.statusIcome()
            dogs.append(dog)
            print(f"Perro Registrado: Status{dog.icomeStatus}")
        if choise == 3:
            for id, dog in enumerate(dogs, start =0):
                print(f"| NumeroID:{id}: | | {dog.__dict__} |")
                print("---------------------------------------")


vetMain()
