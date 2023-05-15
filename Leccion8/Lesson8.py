"""Conceptos basicos de POO Ejercicios de instanciacion """

"""
74. Construir un programa python que declare una clase de tipo ANIMAL y 
que instancie un objeto llamado INSECTO.
"""
class Animal:
    name = 'ant'
    size = "small"
    color = "Green"
    typeAnimal = "Insect"

    def type_structure(self):
        self.typeStructure = "invertebrate"
        return self.typeStructure
    
    def family_animal(self, typeAnimal):
        self.typeAnimal = typeAnimal
        return self.typeAnimal


    
"""
75. Construir un programa python que declare una clase VEHICULO y que instancie
un objeto llamado AVION.
"""
class Vehicle(object):
    def __init__(self, color, model, enrollment, type_vehicle ): 
        self.__color= color
        self.__model= model
        self.__enrollment= enrollment
        self.__type_vehicle= type_vehicle

    #management getter
    @property
    def get_color(self) -> str :
        return self.__color
    @property
    def get_model(self) -> str:
        return self.__model 
    @property
    def enrollment(self) -> int:
        return self.__enrollment
    @property
    def type_vehicle(self) -> str:
        return self.__type_vehicle
    #management setter
    @type_vehicle.setter
    def type_vehicle(self, new_type) -> str:
        print('New name vehicle type')
        self.__type_vehicle = new_type

    @enrollment.setter
    def enrollment(self, new_enrollment)-> int:
        print("New Enrollment vehicle")
        self.__enrollment = new_enrollment
    
    
    

"""
76. Construir un programa python de declares una clase VEHICULO y que instancie 
un objeto llamado CARRO

"""
 
"""
77. Construir un programa python que declare una clase COMIDA y que instancie
ub objeto llamado ARROZCONPOLLO.
"""
class Food:
    pass
"""
78. Construir un programa python que declare una clase ARBOL y que instancie un 
objeto llamado CEDRO.
"""
class Tree:
    pass
"""
79. Construir un programa python que declare una clase LIBRO  y que intancie un 
objeto llamado NOVELA.
"""
class Book:
    pass
"""
80. Construir un programa python que declare una clase  PELICULA  y que instancie un
objeto llamado  MONSTERSINC.
"""
class Movie:
    pass
"""
81. Constuir un programa python que declare una clase DISPOSITIVO  y que instancie un
objeto llamado PORTATIL.
"""
class Device:
    pass
"""
82. Construir un programa python que declare una clase SERVICIO y que instancie un 
objeto llamado ENERGIA.
"""
class Service:
    pass
"""
83. Construir un programa python que declare una clase EMPAQUE  y que instancie un
objeto llamado CAJA.
"""
class Paking: 
    pass