"""
Un concesionario de autos vende vahículos nacionales e importados.
Todos tienen 4 ruedas y capacidad para 5 pasajeros. Esta información
debe registrarse siempre  por razones de ley. Requiere un programa que
le permita almacenar las 10 principales características  de los autos.
el precio  de venta de cada auto es igual al precio de compra multiplicado
por 1.4 que corresponde a su margen de ganancia. 
"""

class vehicles:
    def __init__(self, sourceType:str, purchasePrice:int, vehiclePlaca:str, color:str, engine:int,power:int,torque:int, typeOfBox:str, ):
        self._wheels = 4 
        self._stalls = 5
        self._profitability = 1.4
        self.sourceType = sourceType
        self.salePrice = 0
        self.purchasePrice = purchasePrice
        self.vehiclePlate = vehiclePlaca
        self.color = color
        self.engine= engine
        self.power = power
        self.torque = torque
        self.typeOfBox = typeOfBox