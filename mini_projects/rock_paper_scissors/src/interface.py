import click
import time
import sys
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
    JUGAR->
    SALIR->
    """)
    init_game()

def win_game():
    pass

def game_over():
    pass

def init_game():
    
    control = click.getchar()
    if control == 'j':
        click.echo('init game')
    
    elif control == 'x':
        sys.exit()
    else:
        click.echo(click.style('Preciona la tecla correcta',fg='red', bg='white'))
        time.sleep(3)
        click.clear()
        view()
        