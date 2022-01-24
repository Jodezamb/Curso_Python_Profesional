

# son un tipo de caso especial con 3 reglas 
#1. Tenemos una nesf funcion  
#2.la nest funcion referencia a un valor  de un scoope superior 
#3 este nest funcion es retornada



#progrma hola 3 -> HOLAHOLAHOLA



def make_repeater_of(n):
    def repeater(string):
        assert type(string)==str,'Solo se puede usar cadenda de caracteres'
        return string*n
    return repeater

def run():
    repeta_5=make_repeater_of(5)
    print (repeta_5('Bienvenidos'))

    repeta_10=make_repeater_of(10)
    print (repeta_10(10))


if __name__ == '__main__':
    run()


