""" 
Sombrero, Saco, Zapatos 
"""

class Clothes:
    def name(self, name):
        print("Name Clothes: "+ name)

class Hat(Clothes):
    pass

class Coat(Clothes):
    pass

class Shoes(Clothes):
    pass


data1 = Hat()
data2 = Coat()
data3 = Shoes()

data1.name("Sombrero")
data2.name("Saco")
data3.name("Zapatos")
