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
#Instancias de la clase supperior que se estaba usando
def carro():
    car = Vehicle(color="blue", model="Audi", enrollment= 3331,  type_vehicle="Car")
    print(car.get_model)
    print(car.type_vehicle)
    print(car.get_color)
    print(car.enrollment)
    print("Enrollment change")
    car.enrollment = 356434
    print(car.enrollment)
 
"""
77. Construir un programa python que declare una clase COMIDA y que instancie
ub objeto llamado ARROZCONPOLLO.
"""
class Food:
    def __init__(self,type_eat, name, size, price):
        self.__type_eat : str = type_eat
        self.__name: str = name
        self.__size: str = size
        self.__price: int = price
    
    #management getter
    @property
    def type_eat(self) -> str:
        return self.__type_eat
    
    @property 
    def name(self) -> str:
        return self.__name
    
    @property
    def size(self)-> str:
        return self.__size
    
    @property
    def price(self)-> int:
        return self.__price
   
"""
78. Construir un programa python que declare una clase ARBOL y que instancie un 
objeto llamado CEDRO.
"""
class Tree:
    def __init__(self, size:str, Name:str, family:str):
        self.__size = size
        self.__name = Name
        self.__family = family
    
    @property
    def size (self)-> str:
        return self.__size
    @property
    def name(self)-> str:
        return self.__name
    @property
    def family(self)-> str:
        return self.__family
 
"""
79. Construir un programa python que declare una clase LIBRO  y que intancie un 
objeto llamado NOVELA.
"""
class Book:
    def __init__(self, size, weight, pages, registered, collection, price, name):
        self.size = size
        self.weight =  weight
        self.pages = pages
        self.registered = registered
        self.collection = collection
        self.price = price
        self.name  = name 
    
    def register(self) -> bool:
        self.registered = True
        return 'Registrado'
    

"""
80. Construir un programa python que declare una clase  PELICULA  y que instancie un
objeto llamado  MONSTERSINC.
"""
class Movie:
    def __init__(self,name, weight, gender, years):
        self.name = name
        self.weight = weight
        self.gender = gender
        self.years = years
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