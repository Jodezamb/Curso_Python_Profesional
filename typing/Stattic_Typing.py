
from typing import Dict,List # importacion del modulo typing para dar estructura al momento de definir 

positivies: List[int]=[1,2,3,4,5]  # estructura para definir una lista de enteros 

users: Dict[str,int]={    # estructura para definir una diccionario con su tipoado 
    'Ecuador': 1,
    'Argentina': 2,}

countries: List[Dict[str,int]]=[
    {'ecuador':1,
    'argentina':2

    },
    {'venezuela':1,
    'colombia':2

    }
]

# ventajas
# nos aportar claridad al codigo, nos va a devolver los errores antes de que el programa se ejecuta  sin la necesidad  de que sea un tipado estatico. 

print(positivies)
print(users)
print(countries)