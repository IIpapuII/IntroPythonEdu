
class Person():
    def ID(self, name):
        print(f'Me llamo {name} y soy un ser humano')

class Animal():
    def ID(self, name):
        print(f'Me llamo {name} y soy un perro')

class Tree():
    def ID(self, name):
        print(f'Me llamo {name} y soy un ser humano')

def general(LivingBeing, name):
    LivingBeing.ID(name)

#Declaration of instances (objects)
Man = Person()
Pet = Animal()
Plant = Tree()

general(Man,"Carlos")
general(Pet,"Michii")
general(Plant,"Arboro")
