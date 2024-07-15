from program1.menu import menu as Ej1

print(f'---------Ejecicios Lesición 13------------------')
status = True
while status == True:
    print("Para salir utiliza la opción 6")
    varInput = int(input("Ingrese el ejercio a ejecutar de acuerdo al numero de  1 al 5:> "))
    if varInput == 1:
        Ej1()
    elif varInput ==2:
        pass
    elif varInput == 3:
        pass
    elif varInput == 4:
        pass
    elif varInput == 5:
        pass
    elif varInput == 6:
        status = False
    else: 
        print("Ingrese un valor en el rango del menú")

