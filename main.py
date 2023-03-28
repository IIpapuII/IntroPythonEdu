from Leccion1.LessonOneExerOne import *
from Leccion2.LessonTwoExerTwo import *
from Leccion3.LessonThre import *
from Leccion4.Lessonfour import *
from Lesson5.Lesson5 import *
from Lesson6.Lesson6 import *
from Leccion7.Lesson7 import *

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
    elif Valor == 49:
        text = input('Enter text: ')
        add_string(text)
    elif Valor == 50:
        number_one = (int(input('Enter number one: ')))
        number_two = (int(input('Enter number two: ')))
        greater_data(number_one , number_two)
    elif Valor == 51:
        number = int(input('Enter number: '))
        multiplication_table(number)
    elif Valor == 52:
        number = int(input('Enter number: '))
        last_digit_four(number)
    elif Valor ==53:
        numbers = [343,4534,523452,5444,245,65234]
        last_digit_list(numbers)
    elif Valor == 54:
        number = int(input('Enter number: '))
        data = number_multiples(number)
        for i in data:
            print(i)
        print(list(data))
    elif Valor == 55:
        number =  int(input('Enter number: '))
        data = sum_four_limit(number)   
        print(list(data))
    elif Valor == 56:
        number = int(input('Enter number: '))
        data = equal_number_end(number)
        print(list(data))
    elif Valor == 57:
        number = int(input('Enter number: '))
        data = sum_eight_limit(number)
        print(list(data))
    elif Valor == 58:
        number = int(input('Enter Number: '))
        data = print_number_odd(number)
        print(list(data))
    elif Valor == 59:
        number = int(input('Enter number: '))
        data = print_number_multiples(number)
        print(list(data))
    elif Valor ==  60:
        number_user = int(input('Enter number User '))
        number = int(input('Enter number: '))
        data = number_range_principle(a=number, b=number_user)
        print(list(data))
    elif Valor == 61:
        number = int(input("Enter number: "))
        data = print_number_range(number)
        print(list(data))
    elif Valor == 62:
        number = int(input('Enter number: '))
        data = range_number_principle_multiple(number)
        print(list(data)) 
    elif Valor == 63:
        raising_number()
    else: 
        print('Erro Valor no Encontrado')


if __name__ == '__main__':
    main()