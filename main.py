from Leccion1.LessonOneExerOne import *
from Leccion2.LessonTwoExerTwo import *
from Leccion3.LessonThre import *
from Leccion4.Lessonfour import *
from Lesson5.Lesson5 import *
from Lesson6.Lesson6 import *
from Leccion7.Lesson7 import *
from Leccion8.Lesson8 import *
from Lesson9 import ExerciseFour,ExerciseOne,ExerciseThree,ExerciseTwo

def main():
    Value=int(input('Ingrese el numero de ejecio A desarrollar: '))
    if Value == 1:
        FullName()
    elif Value == 2:
        CentrarTexto()
    elif Value == 3:
        Suma()
    elif Value == 4:
        Producto()
    elif Value == 5:
        Resta()
    elif Value == 6:
        Divicion()
    elif Value == 7:
        Concidencia()
    elif Value == 8:
        concatenar()
    elif Value == 9:
        concatenarEdad()
    elif Value == 10:
        ConcaTotal()
    elif Value == 11:
        Potencia()
    elif Value == 12:
        WholeNumber()
    elif Value == 13:
        LastDigit()
    elif Value == 14:
        SumaTwoDigit()
    elif Value == 15:
        PenultimateDigitPower()
    elif Value == 16:
        remainderofdivision()
    elif Value == 17: 
        addLastDigit()
    elif Value == 18:
        sumThreDigit()
    elif Value == 19:
        chainEquals()
    elif Value == 20: 
        sumComplex()
    elif Value == 21:
        NumerPositiveFour()
    elif Value == 22:
        oddNumber()
    elif Value == 23:
        evenNumber()
    elif Value == 24: 
        lastOddDigit()
    elif Value == 25:
        numberSame()
    elif Value == 26:
        SumLatestSeven()
    elif Value == 27:
        sumBiggerNumber()
    elif Value == 28:
        BiggerNumber()
    elif Value == 29:
        numbeObbCouple()
    elif Value == 30:
        number =  [20,21,30,41,50,51,201]
        NumberArrayOne(number)
    elif Value == 31:
        print_years()
    elif Value == 32:
        print_people_table()
    elif Value == 33:
        vertical_text()
    elif Value == 34:
        letter_repeater()
    elif Value == 35:
        sum_thousand()
    elif Value == 36:
        number_multiples()
    elif Value == 37:
        advanced_by_six()
    elif Value == 38:
        number_months()
    elif Value == 39:
        multiples_of_three()
    elif Value == 40:
        add_pairs()
    elif Value ==41:
        sum_vowels()
    elif Value ==42:
        add_words()
    elif Value == 43:
        add_syllables()
    elif Value == 44:
        name = input ('Enter your name: ')
        print_name(name,5)
    elif Value == 45:
        text = input('Enter text: ')
        amount = int(input('Enter amount: '))
        repeat_text(text,amount)
    elif Value == 46: 
        list_numbers = [2,56,543,45,234,65,4234,675]
        sum_of_number(list_numbers)
    elif Value == 47:
        list_numbers = [4,2,6,2,6,4,2,1]
        average_pairs(list_numbers)
    elif Value == 48:
        list_numbers = [3,543,6,3,32,6,32,456,1,54]
        average_data(list_numbers)
    elif Value == 49:
        text = input('Enter text: ')
        add_string(text)
    elif Value == 50:
        number_one = (int(input('Enter number one: ')))
        number_two = (int(input('Enter number two: ')))
        greater_data(number_one , number_two)
    elif Value == 51:
        number = int(input('Enter number: '))
        multiplication_table(number)
    elif Value == 52:
        number = int(input('Enter number: '))
        last_digit_four(number)
    elif Value ==53:
        numbers = [343,4534,523452,5444,245,65234]
        last_digit_list(numbers)
    elif Value == 54:
        number = int(input('Enter number: '))
        data = number_multiples(number)
        for i in data:
            print(i)
        print(list(data))
    elif Value == 55:
        number =  int(input('Enter number: '))
        data = sum_four_limit(number)   
        print(list(data))
    elif Value == 56:
        number = int(input('Enter number: '))
        data = equal_number_end(number)
        print(list(data))
    elif Value == 57:
        number = int(input('Enter number: '))
        data = sum_eight_limit(number)
        print(list(data))
    elif Value == 58:
        number = int(input('Enter Number: '))
        data = print_number_odd(number)
        print(list(data))
    elif Value == 59:
        number = int(input('Enter number: '))
        data = print_number_multiples(number)
        print(list(data))
    elif Value ==  60:
        number_user = int(input('Enter number User '))
        number = int(input('Enter number: '))
        data = number_range_principle(a=number, b=number_user)
        print(list(data))
    elif Value == 61:
        number = int(input("Enter number: "))
        data = print_number_range(number)
        print(list(data))
    elif Value == 62:
        number = int(input('Enter number: '))
        data = range_number_principle_multiple(number)
        print(list(data)) 
    elif Value == 63:
        raising_number()
    elif Value == 64:
        number = int(input('Enter number'))
        print(sum_number_three(number))
    elif Value == 65:
        print('Result: ',number_sqrt())
    elif Value == 66:
        raising_number()
    elif Value == 67:
        chain_string_len()
    elif Value == 68:
        count_string()
    elif Value == 69:
        count_vocals()
    elif Value == 70:
        count_letter_a()
    elif Value == 71:
        search_user_letter()
    elif Value == 72:
        number_devisor()
    elif Value == 73:
        equal_number_of_lengths()
    elif Value == 74:
        insecto = Animal()
        print("Name= ", insecto.name)
        print("Size=", insecto.size)
        print("Color=", insecto.color)
        print("Type Animal=", insecto.typeAnimal)
        print("Type Structure=", insecto.type_structure())
        print("Family Animal=", insecto.family_animal("Arthropoda"))
    elif Value == 75:
        airplane = Vehicle(color="red", model="boind", enrollment= 3331,  type_vehicle="Airplane")
        print(airplane.get_model)
        print(airplane.type_vehicle)
        print(airplane.get_color)
        print(airplane.enrollment)
        print("Enrollment change")
        airplane.enrollment = 356434
        print(airplane.enrollment)
    elif Value == 76:
        carro()
    elif Value == 77:
        foodRice = Food('Arroz', 'Arroz con pollo', 'Grande', 10000)
        print(foodRice.name)
        print(foodRice.type_eat)
        print(foodRice.size)
        print(foodRice.price)
    elif Value == 78:
        cedro = Tree('Grander', 'Cedro','perenne')
        print(cedro.name)
        print(cedro.size)
        print(cedro.family)
    elif Value == 79:
        novela = Book('14x12','300gms',345, False, 'NoAun', 500000,'fulltime')
        print(novela.size)
        print(novela.weight)
        print(novela.pages)
        print(novela.registered)
        print(novela.collection)
        print(novela.price)
        print(novela.name)
        print(novela.register())
        print(novela.registered)
    #Lesson 8 exercises
    elif Value == 80:
        monster = Movie('monstersinc', '2GB','Fantacia','2015')
        print(monster.name)
        print(monster.weight)
        print(monster.gender)
        print(monster.years)
    #Lesson 9 Exercises
    elif Value == 81:
        ExerciseOne.vetMain()
    elif Value == 82:
        ExerciseTwo.mainStationary()
    elif Value == 83:
        ExerciseThree.mainVahicles()
    elif Value == 84:
        ExerciseFour.mainDevices()
    elif Value == 85:
        pass
    elif Value == 86:
        pass
    elif Value == 87:
        pass
    elif Value == 88:
        pass
    else: 
        print('Erro Value no Encontrado')


if __name__ == '__main__':
    main()