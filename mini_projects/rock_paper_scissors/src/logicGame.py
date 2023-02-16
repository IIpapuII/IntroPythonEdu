import click
import time
import random
import src.interface
punctuation_user = 0
punctuation_machine =0


def logic_game_user(inser_data_game):
    global punctuation_user
    global punctuation_machine
    if  inser_data_game == logic_machine_game():
        print('Empate')
        time.sleep(3)
        src.interface.game()
    elif inser_data_game != logic_machine_game():
        punctuation += 1
        print('Gana Usuario')
        time.sleep(3)
        src.interface.game()
def Score_user():
    global punctuation_user
    return punctuation_user

def Score_machine():
    global punctuation_machine
    return punctuation_machine

def logic_machine_game():
    machine_date = ('A','S','D')
    return machine_date[random.randint(0,2)]


    

