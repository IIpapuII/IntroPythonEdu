"""
Un concesionario de autos vende vahículos nacionales e importados.
Todos tienen 4 ruedas y capacidad para 5 pasajeros. Esta información
debe registrarse siempre  por razones de ley. Requiere un programa que
le permita almacenar las 10 principales características  de los autos.
el precio  de venta de cada auto es igual al precio de compra multiplicado
por 1.4 que corresponde a su margen de ganancia. 
"""

class vehicles:
    def __init__(self, sourceType:str, purchasePrice:int, vehiclePlaca:str, color:str, engine:float,power:float,torque:float, typeOfBox:str, ):
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


    def calculPriceVehicle(self):
        self.salePrice = self.purchasePrice * self._profitability
    
    def EnterData():
        choiseSourse =  int(input("Ingrese el valor según el tipo de vehiculo a registrar: 1- Nacionales 2- Importados: " ))
        if choiseSourse == 1:
            sourseType = 'Nacionales'
        elif choiseSourse  == 2:
            sourseType = 'Importados'
        else:
            print('Incorrect selection')
        
        purchasePrice = int(input("Ingrese el precio del compra del  vehiculo: "))
        vehiclePlaca = input("Ingrese la placa de registro del vehiculo: ")
        color = input("Ingrese el color del vehiculo: ")
        engine = float(input("Ingrese el tipo de motor del vehiculo: "))
        power = float(input("Ingrese la potencia del motor: "))
        torque= float(input("Ingrese el torque que maneja el vehiculo: "))

        choiseTypeBox = int(input("Ingrese el tipo de caja que maneja el Vehiculo: 1- Automatica 2-Manual: "))
        if choiseTypeBox == 1:
            typeOfBox = 'Automatica'
        elif choiseTypeBox == 2:
            typeOfBox = 'Manual'
        else:
            print('Incorrect selection')

        return sourseType.upper(), purchasePrice, vehiclePlaca.upper(), color, engine, power, torque, typeOfBox.upper()

def mainVahicles():
    dataVehicle = []
    while True:
        print("----------------------Consecionario--------------------------")
        choise = int(input("""¿Desea registrar un nuevo Vehiculo? 
                           1-SI 
                           2-NO
                           3-lISTAR REGISTROS 
                           : """))
        if choise == 2:
            break
        if choise == 1:
            inputVehicle = vehicles(*vehicles.EnterData())
            inputVehicle.calculPriceVehicle()
            dataVehicle.append(inputVehicle)
            print("Se ingreso el vehiculo de manera correcta")
        if choise == 3:
            for i, data in enumerate(dataVehicle, 1):
                print("---------------------------------------------------------------------")
                print(f'id: {i}, | result: {data.__dict__}')
                