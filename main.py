from Leccion1.LessonOneExerOne import *
from Leccion2.LessonTwoExerTwo import *
from Leccion3.LessonThre import *
from Leccion4.Lessonfour import *
from Lesson5.Lesson5 import *



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
    elif Valor == 33:
        vertical_text()
    elif Valor == 34:
        letter_repeater()
    elif Valor == 35:
        sum_thousand()
    elif Valor == 36:
        number_multiples()
    elif Valor == 37:
        advanced_by_six()
    elif Valor == 38:
        number_months()
    elif Valor == 39:
        multiples_of_three()
    elif Valor == 40:
        add_pairs()
    elif Valor ==41:
        sum_vowels()
    elif Valor ==42:
        add_words()
    elif Valor == 43:
        add_syllables()
    elif Valor == 44:
        name = input ('Enter your name: ')
        print_name(name,5)
    elif Valor == 45:
        text = input('Enter text: ')
        amount = int(input('Enter amount: '))
        repeat_text(text,amount)
    elif Valor == 46: 
        list_numbers = [2,56,543,45,234,65,4234,675]
        sum_of_number(list_numbers)
    elif Valor == 47:
        list_numbers = [4,2,6,2,6,4,2,1]
        average_pairs(list_numbers)
    elif Valor == 48:
        list_numbers = [3,543,6,3,32,6,32,456,1,54]
        average_data(list_numbers)
    else: 
        print('Erro Valor no Encontrado')

if __name__ == '__main__':
    main()