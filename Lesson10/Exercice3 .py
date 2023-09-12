#Pelicula -> Humor -> Colombiana

class pelicula:
    pass

class Humor(pelicula):
    def __init__(self,name, gener, duration) -> None:
        super().__init__()
        self.name = name
        self.gener = gener
        self.duration = duration

class colombiana(Humor):
    pass

peli = pelicula
peliHumor = Humor("Pelicula","Comedia",2)
peliColombiana = colombiana("EL paseo","Comedia",3)
print(peli.__dict__)