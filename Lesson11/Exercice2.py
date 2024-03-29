"""
Pancho(Perro), Lulu(gata), Teresita(Iguana)
"""

class animal:
    def name(self, name):
        print(name)

class Dog(animal):
    pass

class Cat(animal):
    pass

class Iguana(animal):
    pass
    

perro = Dog()
Gato = Cat()
iguana = Iguana()


perro.name("pancho")
Gato.name("lulo")
iguana.name("Teresita")




