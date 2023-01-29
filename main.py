from Leccion1.LessonOneExerOne import *
from Leccion2.LessonTwoExerTwo import *
from Leccion3.LessonThre import *
from Leccion4.Lessonfour import *


def main():
    Valor=int(input('Ingrese el numero de ejecio A desarrollar: '))
    if Valor == 1:
        FullName()
    elif Valor == 2:
        CentrarTexto()
    elif Valor == 3:
        Suma()
    elif Valor == 4:
        Producto()
    elif Valor == 5:
        Resta()
    elif Valor == 6:
        Divicion()
    elif Valor == 7:
        Concidencia()
    elif Valor == 8:
        concatenar()
    elif Valor == 9:
        concatenarEdad()
    elif Valor == 10:
        ConcaTotal()
    elif Valor == 11:
        Potencia()
    elif Valor == 12:
        WholeNumber()
    elif Valor == 13:
        LastDigit()
    elif Valor == 14:
        SumaTwoDigit()
    elif Valor == 15:
        PenultimateDigitPower()
    elif Valor == 16:
        remainderofdivision()
    elif Valor == 17: 
        addLastDigit()
    elif Valor == 18:
        sumThreDigit()
    elif Valor == 19:
        chainEquals()
    elif Valor == 20: 
        sumComplex()
    elif Valor == 21:
        NumerPositiveFour()
    elif Valor == 22:
        oddNumber()
    elif Valor == 23:
        evenNumber()
    elif Valor == 24: 
        lastOddDigit()
    elif Valor == 25:
        numberSame()
    elif Valor == 26:
        SumLatestSeven()
    elif Valor == 27:
        sumBiggerNumber()
    elif Valor == 28:
        BiggerNumber()
    elif Valor == 29:
        numbeObbCouple()
    elif Valor == 30:
        number =  [20,21,30,41,50,51,201]
        NumberArrayOne(number)
    elif Valor == 31:
        print_years()
    elif Valor == 32:
        print_people_table()
    else: 
        print('Erro Valor no Encontrado')

if __name__ == '__main__':
    main()