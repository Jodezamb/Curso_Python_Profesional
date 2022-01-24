from itertools import count
import time

def fibo_gen():
    n1=0
    n2=1
    counter=0
    while True:
        if counter ==0:
            counter+=1
            '''recordar que la palabra yield es 
            como la palabra return solo que esta  guarda 
            el estado en que la funcion retorna y continua en el siguien yield 
            cuando la funcion se ejcuta nuevamente
            a diferncia de return que sale de la funcion'''
            
            #resumen yiel paisa el estado de la funcion
            yield n1 
        elif counter ==1:
            counter+=1
            yield n2
        else:
            aux = n1 +n2
            n1,n2=n2, aux
            counter+=1
            yield aux
if __name__ == '__main__':
    fibonacci =fibo_gen()
    for element in fibonacci:
        print(element)
        time.sleep(1)
            