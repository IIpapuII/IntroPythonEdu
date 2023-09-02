"""
Un almacén vende dispositivos  electrónicos (Celualres, tablets y portátiles).
Todos PHR que es una nueva marca que está entrando en el mercado.
Se requiere almacenar sus 6 principales características. Todos son
productos importados  y su precio de venta es igual a su precio de compra 
multiplicado por 1.7 que corresponde  a su margen de ganancia.  
"""
class  Devices:
    def __init__(self, typeOfDevices:str,ram:int, storage:int, purchasePrice:int):
        self.typeOfDevices = typeOfDevices
        self.brand = 'PHR'
        self.ram = ram
        self.storage = storage
        self.salesPrice = 0
        self.PurchasePrice = purchasePrice
        self.profitability = 1.7
    
    def calcSalesPrice(self):
        self.salesPrice = self.PurchasePrice * self.profitability
    
    def inputDataDevices():
        choiseTypeDevices = int(input("Ingrese la selección del tipo de dispositivo : 1- Celulares 2- Tablets 3- Portátiles:"))
        if choiseTypeDevices == 1:
            typeOfDevices = 'Celulares'
        elif choiseTypeDevices == 2:
            typeOfDevices = 'Tablets'
        elif choiseTypeDevices  == 3:
            typeOfDevices = 'Portatiles'
        else:
            print("Selección incorrecta")
        ram = int(input("Ingrese la cantidad de RAM del dispositivo: "))
        storage = int(input("Ingrese la cantidad de almacenamiento del dispositivo: "))
        purchasePrice = int(input("Ingrese el precio de compra: "))
        return typeOfDevices, ram, storage, purchasePrice

def mainDevices():
    dataDevices = []
    while True:
        print("----------------------Consecionario--------------------------")
        choise = int(input("""¿Desea registrar un nuevo Equipo? 
                           1-SI 
                           2-NO
                           3-lISTAR REGISTROS 
                           : """))
        if choise == 2:
            break
        if choise == 1:
            inputDevices = Devices(*Devices.inputDataDevices())
            inputDevices.calcSalesPrice()
            dataDevices.append(inputDevices)
            print("Se ingreso el vehiculo de manera correcta")
        if choise == 3:
            for i, data in enumerate(dataDevices, 1):
                print("---------------------------------------------------------------------")
                print(f'id: {i}, | result: {data.__dict__}')

mainDevices()