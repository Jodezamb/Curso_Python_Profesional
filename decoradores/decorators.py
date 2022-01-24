from datetime import datetime

#  creacion de un decorador para poder averiguar cuanto tiempo tarde en ejectarse una funcion 
# analizar eficiencia

def execution_time(func):
    def wrapper():
        initial_time=datetime.now()
        func()
        final_time=datetime.now()
        time_elapsed=final_time-initial_time
        print("Pasaron ", time_elapsed.total_seconds()," segundos")
    return wrapper

@execution_time  # decorador 
def random_func():
    for _ in range (1,100000000):
        pass

random_func()