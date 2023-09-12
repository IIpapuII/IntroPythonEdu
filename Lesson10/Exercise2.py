#Libro -> Novela -> Romantica

class Libro:
    pass

class Novela(Libro):
    def __init__(self, name, gender, price ):
        self.name = name
        self.gender = gender
        self.price = price

class Romantica(Novela):
    pass

book = Libro

BookNovela = Novela("Novela","Romantico","23000")
bookRomantico = Romantica("Lux Da","Fantacia romantica","36552")
print(bookRomantico.__dict__)