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
