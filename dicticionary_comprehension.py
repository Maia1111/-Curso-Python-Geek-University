"""
Dictionary Comprehension

Pense no seguinte:
Se quisermos criar uma lista fazemos:

lista = [1, 2, 3, 4]

Se quisermos  cruar uma tupla
tupla = (1, 2, 3, 4)


Se quisermos criar um set 
conjunto = {1, 2, 3, 4}

Se quisermos criar um dicionário
dicionário = {'a': 1, 'b': 2, 'c': 3, 'd': 4}


Sintaxe para dictionary comprehension 

{chave:valor for valor in iterável}
"""

# Exemplos
numeros = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

quadrado = {chave: valor ** 2 for chave, valor in numeros.items()}

print(quadrado)

# Gerando uma list Comprehension apartir de uma lista de  numeros
numeros = [1, 2, 3, 4, 5]

quadrados = {valor: valor ** 2 for valor in numeros}
print(quadrados)

# Misturando dados de duas variáveis em um dicionario 
chaves = 'abcde'
valores = [1, 2, 3, 4, 5]

mistura = {chaves[i]: valores[i] for i in range(0, len(chaves))}
print(mistura)


# Exemplo com logica condicional
res = {num: ('par' if num % 2 == 0 else 'impar') for num in numeros}
print(res)