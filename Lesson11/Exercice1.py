""" 
Utilizar el recurso del polimorfismo  en python para mostrar datos de la siguientes clases
"No me olvides nunca" (ObraMusical), "El beso"(Escultura), "Amacer" (Pintura)
"""

class MusicalPiece():
    def title(self, name):
        print(f'El nombre de la obra musical es: {name}')

class Sculpture():
    def title(self, name):
        print(f'El nombre de la escultura es: {name}')

class Paint():
    def title(self, name):
        print(f'El nombre de la pintura es: {name}')


def general(TypeOfArt, name):
    TypeOfArt.title(name)


Musica = MusicalPiece()
Escultura = Sculpture()
Pintura = Paint()

general(Musica, "No me olvides nunca")
general(Escultura, "El beso")
general(Pintura, "Amacer")