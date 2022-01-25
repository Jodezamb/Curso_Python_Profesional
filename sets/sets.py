# Un set es una estrcutura de dato que guarda elementos 
# de manera inmutable y no repetidos. 




set1={1,2,3,4}
set2={4,5,6,7}

'''set1.union(set2)
set1.symmetric_difference(set2)
set1.difference(set2)
set1.intersection(set2)'''

#union
setunion=set1.union(set2)
print(setunion)
#interseccion
interseccionSet=set1&set2
print(interseccionSet)

#diferrence
differenceSet=set2-set1
print(differenceSet)

#symetric_Dif_Set
symetric_Dif_Set=set1^set2
print(symetric_Dif_Set)


'''Crear una funcion que elimine los elemento repetidos por medio de for y set'''

def eliminar(lista):
    without_List=[]
    for element in lista:
        if element not in without_List:
            without_List.append(element)
    return without_List

def eliminar_with_set(lista):
    return list(set(lista))

    
def run():
    random_list=[1,2,3,1,1]
    print(eliminar(random_list))
    print(eliminar_with_set(random_list))


if __name__ == '__main__':
    run()
