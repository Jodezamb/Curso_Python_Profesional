from datetime import datetime

#  creacion de un decorador para poder averiguar cuanto tiempo tarde en ejectarse una funcion 
# analizar eficiencia

def execution_time(func):
    def wrapper(*args,**kwargs): # estos parametros son para que pueda funcionar cualquier funcion, no importa l cantida de argumentos posicionales que se le envie 
        initial_time=datetime.now() # la funcion lo va a recibir, * es el operador de desestructuracion,  *kwargs no importa la cantida de parametros nombrados se va a ejecutar
        func(*args,**kwargs)
        final_time=datetime.now()
        time_elapsed=final_time-initial_time
        print("Pasaron "+str(time_elapsed.total_seconds())+" segundos")
    return wrapper

@execution_time  # decorador 
def random_func():
    for _ in range (1,100000000):
        pass
@execution_time
def suma(a: int,b: int)-> int:
    return a+b
@execution_time
def saludo(nombre="adrian"):
    print('hola ',nombre)

suma(5,5)
random_func()
saludo('Jose')