"""
listas

Listas em Python funciona como vetores/matrizes (arrays) em outras linguagens, como a diferença de serem dinanâmicos
e também de podermos colocar    QUALQUER     TIPO DE DADOS.

- Dinâmico: podemos criar a lista e ir adicionando elementos
podemos adicionar elementos enqquanto tiver memória do computador suficiente

As listas são representadas por []

Podemos facilmente ordenar uma lista

"""

lista1 = [1, 2, 3, 0, 78, 65, 51, 91]

lista2 = ['G', 'e', 'e', 'k', 'u', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']

lista3 = []

lista4 = list(range(11))

# Podemos facilmente ordenar uma lista


lista1.sort()
print(lista1)

lista5 = list('Geek University')

lista5.sort()
print(lista5)

# Podemos contar facilmente o numero de ocorrência de um elemento dentro de uma lista.
print(lista5.count('e'))


# Adicionar elementos em listas
"""
Para adionar elementos em listas utilizamos a função append

Com append nós só conseguimos adicionar um elemento por vez

"""

lista1.append(42)
print(lista1)

# A Função extend extende uma lista para outra lista ( Só aceita iteravéis)
lista1.extend([1, 2, 4])
print(lista1)


# Podemos facilmente remover o ultimo elemento de uma lista
print(lista5)

# Apagando  o ultimo elemento com função pop
# O pop remove e retorna o elemento que ele remove
lista5.pop()
print(lista5)

# Podemos no pop especificar o indice que quero remover
lista5.pop(2)  # Se não houver um elemento na posição infomada  teremos IndexError
print(lista5)

# Podemos facilmente repetir elementos de uma lista em Python
nova = [1, 2, 3]
print(nova)
nova = nova * 3
print(nova)

# Podemos facilmente converter uma string para lista com split
# OBS: a função split  por padrão separa as strings pelo espaço entre elas
curso = 'Programação em Python: Essencial'
print(curso)
curso = curso.split()
print(curso)

# Convertendo uma lista em uma string
lista6 = ['Programação', 'em', 'Python:', 'Essencial']
print(lista6)

# Abaixo estamos falando: Pega a lista6, coloca espaço entre cada elemento e transforma em uma string
curso = ' '.join(lista6)
print(curso)

# Podemos cria uma lista com elementos de tipos variados, a lista aceita qualquer tipo de dados
lista7 = [1, 2.34, True, 'Geek', 'd', [1, 2, 3], 45678900]
print(lista7)

# Iterando sobre lista Exemplo 1 - utilizando for
for elemento in lista1:
    print(elemento)

# Iterando sobre lista Exemplo 2 - Utilizando while

produto = ''
carrinho = []

while produto != 'sair':
    produto = input('Digite um produto ou sair: ')
    if produto != 'sair':
        carrinho.append(produto)

if carrinho:
    for itens in carrinho:
        print(itens)
else:
    print('Seu carrinho esta vazio!')

# Fazemos acesso aos elementos de forma indexada
#            0         1        2       3
cores = ['verde', 'amarelo', 'azul', 'branco']
print(cores[0])
print(cores[1])
print(cores[2])
print(cores[3])

# mostrando os elementos de forma inversa
print(cores[::-1])
