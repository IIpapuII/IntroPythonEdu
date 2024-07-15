from manage import Pets
def menu():
    status = True
    while status == True:
        print(f'-----------------------------------------------------------')
        print(f'---------------Control de tamaño de mascota----------------')
        print(f'-----------------------------------------------------------')
        VarInput = input("""Ingrese numero:
                      1-Para registrar su mascota y conocer el tamaño
                      2- Salir
                        :::::::| """)
        
        if int(VarInput)==1:
            inputName = input("Ingrese Nombre de la mascosa: ")
            inputPeso = input("Ingrese el peso de la mascota: ")
            inputRaza = input("Ingrese la raza de la mascota: ")
            Mascota = Pets(name=inputName, peso=int(inputPeso), raza= inputRaza)
            print(f'El tamaño de su mascota es el siguiente de acuerdo al peso {Mascota.peso}: {Mascota.identify_size()}')
        elif int(VarInput) == 2:
            status = False
        else:
            print("Ingrese un dato que corresponda al menu")

menu()
        
    