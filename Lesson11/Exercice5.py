""" 
Computador, Tablet, celular
"""

class Technological_equipment:
    def name(self, name):
        print(name)


class Computer(Technological_equipment):
    pass

class Tablet(Technological_equipment):
    pass

class Phone(Technological_equipment):
    pass


data1 = Computer()
data2 = Tablet()
data3 = Phone()

data1.name("Computador")
data2.name("Tableta")
data3.name("Celular")