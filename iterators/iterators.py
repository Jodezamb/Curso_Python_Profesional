import time


class FiboIter():

    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        self.counter = 0
        return self


    def __next__(self):
        if self.counter ==0:
            self.counter+=1
            return self.n1
        elif self.counter ==1:
            self.counter+=1
            return self.n2
        else:
            self.aux =self.n1 + self.n2
            #self.n1 = self.n2
            #self.n2 =self.aux
            # concepto de swap
            self.n1,self.n2=self.n2, self.aux
            return self.aux


if __name__ == '__main__':
    '''se instancia la clase Fiboiter para Obtener un objeto 
    Fiboiter'''
    fibonacci=FiboIter()
    ''' Para recorrer un iterador con un ciclo for sugar sintax '''
    for element in fibonacci:
        print(element)




