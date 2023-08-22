""" 
Una papeliria vende cuadernos y lápices. Los cuadernos pueden ser de  50 hojas
 o 100 hojas. Los lápices pueden ser de grafito o  de colores. El precio de venta
 es igual al precio  de compra multiplicado por 1.30 que corresponde al margen de ganancia.
 La papelería requiere construir un programa que le permita registrar y visualizar por lo menos dos artículos
 de item. Todos los cuaderonos son marca HOJITAS y los lápices son marca RAYAS ya que la 
 papelería en un distribuidor exclusivo.
"""

class Stationary:
    
    def __init__(self,quanty:int,price:int,typeArticle:str):
        self.typeOfArticle = typeArticle
        self.quantity = quanty
        self.typeBook = ""
        self.typePencils = ""
        self._profitability = 1.30
        self.purchasePrice = price
        self.saleValue = 0
        self.inventoryValue = 0
    @property
    def profitability(self) -> int:
        return self._profitability
    
    def calcuSaleValue(self):
        self.saleValue = self.purchasePrice * self.profitability
        self.inventoryValue = self.quantity * self.purchasePrice

    def bookTypeIcome(self):
        typeInput = int(input("""Se presentan dos tipos de libro: 1- 50Hojas 2- 100Hojas : """))
        if typeInput == 1:
            self.typeBook = "50 Hojas"
        elif typeInput == 2:
            self.typeBook = "100 hojas"
        else:
            print("Selection error not valid")

    def pencilsTypeIcome(self):
        typeInput = int(input("""Se presenta dos tipos de lapíces: 1- Grafito 2- Colores : """))
        if typeInput == 1:
            self.typePencils = "Grafito"
        elif typeInput == 2:
            self.typePencils = "Colores"
        else:
            print("seletion error not valid")
    
    def inputDataElement():
        typeInput = int(input("""Se presenta dos tipos de articulos: 1- Cuadernos 2- Lapíces : """))
        if typeInput == 1:
            typearticle = "Cuadernos"
        elif typeInput == 2:
            typearticle = "Lapíces"
        else:
            print("seletion error not valid") 
        quanty = int(input("Ingrese la cantidad de articulos aquiridos: "))
        price = int(input("Ingrese el precio de compra del articulo: "))
        return quanty, price, typearticle
    

def mainStationary():
    ArticleDB= []
    while True:
        print("""-----------------------PAPELIRIA PYTHON----------------------------------""")
        choise = int(input("""¿Desea registrar un nuevo articulo? 
                           1-SI 
                           2-NO
                           3-lISTAR REGISTROS 
                           : """))
        if choise == 2:
            break
        if choise == 1:
            data = Stationary(*Stationary.inputDataElement())
            if data.typeOfArticle == "Cuadernos":
                data.bookTypeIcome()
                data.calcuSaleValue()
            else:
                data.pencilsTypeIcome()
                data.calcuSaleValue()
            ArticleDB.append(data)
            print("Articulo Registrado")
        if choise == 3:
            for id , data in enumerate (ArticleDB, 1):
                print(f"id:{id}| articulo:{data.typeOfArticle}: {data.__dict__}")


mainStationary()