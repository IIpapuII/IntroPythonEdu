""" 
Libro, Revista, Periódico
"""

class Library:
    def name(self,name):
        print(name)


class book(Library):
    pass

class Magazine(Library):
    pass

class newspaper(Library):
    pass

data1 = book()
data2 =  Magazine()
data3 = newspaper()

data1.name("Libro")
data2.name("Revista")
data3.name("Periodico")
