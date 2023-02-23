
import time
import random
import src.interface
punctuation_user = 0
punctuation_machine =0



def Score_user():
    global punctuation_user
    return punctuation_user

def Score_machine():
    global punctuation_machine
    return punctuation_machine

def logic_machine_game():
    machine_date = ('A','S','D')
    return machine_date[random.randint(0,2)]

def logic_game_user(inser_data_game):
    global punctuation_user
    global punctuation_machine
    value_machine = logic_machine_game()
    if  inser_data_game == value_machine:
        print('Empate')
        time.sleep(2)
        src.interface.game()
    elif (inser_data_game == 'A' and value_machine== 'D'):
        punctuation_user += 1
        src.interface.win_game()
    elif inser_data_game == 'S' and value_machine == 'A':
        punctuation_user += 1
        print('Gana Usuario')
        time.sleep(3)
        src.interface.game()     
    elif inser_data_game == 'D' and value_machine == 'S':
        punctuation_user += 1
        print('Gana Usuario')
        time.sleep(3)
        src.interface.game()
    else:
        punctuation_machine += 1
        print('Gana Maquina con: {}'.format(value_machine))
        time.sleep(3)
        src.interface.game()