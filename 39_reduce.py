"""
Reduce

OBS: A partir do Python3  e versões acima reduce() não é mais uma função integrada (built-in).
Agora para utilizar esta função temos que importar do modulo 'functools'.

Guido Van Rossum: utilize a função reduce() se você realmente precisa dela. 
Em todo caso, 99% das vezes um loop for e mais legível.


Para entender o reduce()

# Imagine que você tem uma coleção de dados:
dados = [a1, a2, a3, an]

# E você tem uma função que recebe dois parâmetro: uma função é um iterável


def funcao(x, y):
    return x * y
    
Assim como map() e filter(), a função reduce() recebe dois valores: a função e um iterável,
como mencionado.

reduce(funcao, dados)


A Função reduce(), funciona da seguinte forma:
     Passo 1: res = ela pega dos dois primeiros elementos do iterável e passa para função
     Passo 2: res2 = ela pega o  resultado do processamento dos dois primeiros elementos e processa
     com o terceiro elemento. Isso é repetido até o final

"""

# Exemplo
from functools import reduce

dados = [1, 2, 3, 4, 5, 6, 7, 8]

# função
mult = lambda x, y: x * y 

res = reduce(mult, dados)
print(res)