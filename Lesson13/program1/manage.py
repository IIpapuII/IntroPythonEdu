
class Pets():
    """
    Construir un programa que lea, por lo menos, tres datos de un perro mascota y determine,
    por su altura, si es perro grande, mediano o pequeño.
    """
    
    def __init__(self, name, peso, raza):
        self.name  = name
        self.peso = peso
        self.raza = raza
    

    def  identify_size(self,):
        if self.peso < 10:
            return "Pequeño"
        elif self.peso > 10 and self.peso < 20:
            return "Mediano"
        else:
            return "Grande"

