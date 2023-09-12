#Mamifero -> Domestico -> perro

class mamifero():
    def __init__(self, name, species, color ) -> None:
        self.name = name
        self.species = species
        self.color = color

class domestico(mamifero):
    pass

class perro(domestico):
    pass


animal = mamifero("cuadrupedo","salvaje","negro")
animalDomestico = domestico("Perro","ladrador","Amarillo")
animalperro = perro("Juan","pincher","Negro")
print("Domestico: " + animalDomestico.__dict__)