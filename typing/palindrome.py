


#conceptp
#crear una funcion para saber si una palabra un palindromo, 
# palindromo es cuando una palabra se escribe igual al revez y al derecho 

def is_palindrome(string: str)-> bool:
    string =string.replace(' ','').lower()  # en este paso se realiza un tratamiento al string todo en minuscula y se quita lo espacios. 
    return string==string[::-1]  # se retorna el valor boleano  de comparar el string al revez. 



def run():
    print(is_palindrome(1000)) #error  ya que la funcion espera  recibir un string no un int


if __name__ == '__main__':
    run()
 