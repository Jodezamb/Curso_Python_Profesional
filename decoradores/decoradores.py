# un decorador es una funcion que recibe como parameto otra funcion, le anade cosas, y retorna una funcion diferente. un decoraodor tambien es un clousere especial 

from tkinter import W
from importlib_metadata import re


def mayasculas(func):
    def wrapper(texto): # funcuon envoltutas 
        return func(texto).upper()  # modifica la funcion que ingresa
    return wrapper  #retorna la funcion envoltura


@mayasculas
def mensaje(nombre):
    return f'{nombre}, recibistes un mensaje'

print(mensaje("Adrian"))



