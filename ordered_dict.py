"""
Módulo Collections: Ordered Dict

# Em um dicionário  que nos garante a  ordem de inserção dos elementos e tem um performance melhor que o dicionáro
normal.

dicionario = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})

from collections import OrderedDict

# usando o OrderedDict a ordemm dos elemento são garantidas
dicionario = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})

# Fazendo um for e tendo a ordem dos elementos garantidas
for chave, valor in dicionario.items():
    print(f'Chave:{chave}  valor:{valor}')




"""
from collections import OrderedDict
# Entendendo a diferença entre Dict e um OrderedDict

# Dicionário comum
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 2, 'a': 1}
print(dict1 == dict2)  # Vai retornar True -> já que a ordem nos dicionário não importam

odict1 = OrderedDict({'a': 1, 'b': 2})
odict2 = OrderedDict({'b': 2, 'a': 1})

print(odict1 == odict2)  # Aqui vai dar False -> OrderedDict Quarda a posição dos elementos
