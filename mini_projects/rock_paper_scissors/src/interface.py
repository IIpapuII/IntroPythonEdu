import click
import time
import sys
from src.logicGame import logic_game_user,Score
@click.command()
def view():
    logo = open('D:/Project_code/IntroPythonEdu/mini_projects/rock_paper_scissors/src/output.txt','r')
    color = ('green', 'red', 'blue', 'bright_blue', 'bright_cyan', 'bright_magenta')
    text = logo.read()
    for i in range(len(color)):
        if i ==0:
            click.clear()
        if i < len(color) - 1:
            click.echo(click.style(text, fg=color[i]))
            time.sleep(1)
            click.clear()
        else:
            click.echo(click.style(text, fg=color[i]))
        
    print(
    """
    Selecciona J para jugar y X para salir.
    JUGAR-> J
    SALIR-> X
    """)
    init_game()

def win_game():
    pass

def game_over():
    pass

#control de inicio del Game
def init_game():
    
    control = click.getchar()
    if control.lower() == 'j':
        game()
    
    elif control.lower() == 'x':
        sys.exit()
    else:
        click.echo(click.style('Preciona la tecla correcta',fg='red', bg='white'))
        time.sleep(3)
        click.clear()
        view()

#control visual dentro del Juego
@click.command()
def game():
    click.clear()
    click.echo(click.style("""
    Inicio del juego                                             SCORE :: {}
    __________________
    Reglas de juego:
    Preciona A para tirar piedra -> A
    Preciona S para tirar papel -> S
    Preciona D para tirar tijera -> D
    Preciona X para Salir del Game -> X

    """.format(Score()),fg='blue'))
    inser_game = click.getchar().upper()
    
    if inser_game == 'A' or inser_game == 'S' or inser_game =='D':
        logic_game_user(inser_game)
    elif inser_game == 'X':
        view()
    else:
        game()