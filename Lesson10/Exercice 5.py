#Dispositivo -> computador -> portatil

class dispositivo:
    pass

class computador:
    def __init__(self, name, marca, price) -> None:
        self.name = name
        self.marca = marca
        self.price = price 
    
class portatil(computador):
    pass
