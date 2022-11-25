"""
Modulo Collections - Named Tuple

# Relembrar tupla comum
tupla = (1, 2, 3)
print(tupla[1])

Named tuple -> São tuplas diferenciadas, onde especificamos um nome para as mesmas e também parâmetros

"""
# Importando
from collections import namedtuple

# Precisamos definir o nome e parâmetros

# Forma 1 - Declaração Named Tuple
cachorro = namedtuple('cachorro', 'idade raca nome')

# Forma 2 - Declaração
cachorro = namedtuple('cachorro', 'idade, raca, nome')

# Forma 3 - Declaração (forma mais clara)
cachorro = namedtuple('cachorro', ['idade', 'raca', 'nome'])


# Usando
ray = cachorro(idade=2, raca='Chow chow', nome='Ray')
print(ray)


# Acessando os dados dos elementos pelo indice

# Forma  1 - Pegando pelo indice
print(ray[0])
print(ray[1])
print(ray[2])

# Forma 2 - Pegando pelo nome da variável
print(ray.idade)
print(ray.raca)
print(ray.nome)
