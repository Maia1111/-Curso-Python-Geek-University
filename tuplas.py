"""
Tuplas (tuples)

Tuplas são bastantes parecidas com listas.
Existem basicamente duas diferenças:
 1 - As tuplas são representadas parênteses ()
 2 - As tuplas são imutavéis:Isso significa que ao criar uma tupla ela não muda. Toda
 operação em uma tupla gera uma nova tupla.

"""

# CUIDADO 1:  AS TUPLAS SÃO REPRESENTADAS POR PARÊNTESES
tupla1 = (1, 2, 3, 4, 5, 6)
print(tupla1)

tupla2 = 1, 2, 3, 4, 5, 6
print(tupla2)

# CUIDADO 2: Tuplas com 1 elemento
tupla3 = (4)   # Isso não é uma tupla
print(type(tupla3))

tupla4 = (4, )  # Isso é uma tupla!
print(tupla4)
print(type(tupla4))

# CONCLUSÃO: Podemos concluir definidas principalmente pela virgula e não pelos parênteses

tupla5 = ('Geek University', 'Programação em Python')

escola, curso = tupla5
print(escola)
print(curso)

# OBS Gera erro se colocarmos um numero de variaveris dirente para desempacotar

# Médotos para remoçã e adição nao existem em tupla

tupla6 = (1, 2, 3, 4, 5, 6)
# Podemos  utilizar metodos que fazem operações caso seja todos numeros inteiros ou reais

print(sum(tupla6))
print(max(tupla6))
print(min(tupla6))
print(len(tupla6))


# Tuplas são imutáveis, mais não são bloqueadas para sobescrever

tupla = ('a', 'b', 'c', 'e', 'a', 'b')
print(tupla.count('c'))

escola = tuple('Geek University')
print(escola)
print(escola.count('e'))


# Dicas na utilização de tuplas
# Devemos utilizar tuplas sempre que não precisarmos moficicarmos dados contidos em uma coleção


# Exemplo 1

meses = ('Janeiro', 'Feveiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')

# Iterar sobre uma tupla utilizando while

i = 0

while i < len(meses):
    print(meses[i])
    i = i + 1

# Verrificando em que indece um elemento esta na tupla

print(meses.index('Julho'))
# Caso o elemento não exista  vai gerar um erro ValueError


# Slicing
# tupla [inicio:fim:passo]

print(meses[0:])
print(meses[::-1])
print(meses[5:9])

# Porque utilizar tuplas
# - Tuplas são mais rapidas doque lista
# - Tuplas deixam seu código mais seguro

# Copiando uma tupĺa para outra
tupla = (1, 2, 3)
print(tupla)

nova = tupla
print(nova)
print(tupla)

outra = (4, 5, 6)

# Aqui é feito uma concatenação de tupla
# Quando imprimimos a nova ela volta com mesmo conteúdo sem alterações
nova = nova + outra
print(nova)
print(tupla)

dir(tupla)
