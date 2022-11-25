"""
Conjuntos

- Conjuntos em qualquer liguagem de programação, estamos falando referências à Teoria dos conjuntos da Matemática

- Aqui em Python, os conjuntos são chamados de sets

Dito isto, da mesma forma que na matemática

-Sets (conjuntos) não possuem valores duplicados;
-Sets (Conjuntos) não possuem  valores ordenados;
- Elementos não são acessados via índece nos conjuntos, ou seja, conjuntos não são indexados;

Conjuntos são  bons para se utilizar quando presisamos armazenar elementos
mais nõa nos importamos com a ordenação deles , valores e itens duplicados

Os conjuntos (sets) são referenciados em Python com chaves {} assim como os dicionário, mais em sets só temos valores
não temos chaves

"""
# Definindo um sets(conjunto)

# Forma 1
s = set({1, 2, 3, 4, 5, 5, 6, 7, 2, 3})
print(type(s))
print(s)

# OBS : ao criamos um conjunto, caso seja adicionado um valor já existente , o mesmo
# será ignorado sem gerar error e não fará parte do conjunto

# Forma 2 - Mais comum
s = {1, 2,  3, 4, 4, 5, 5}
print(type(s))
print(s)

# Podemos verificar se determinado elemento esta contido no conjunto
if 3 in s:
    print('Tem o 3')
else:
    print('Não tem o 3')


# Importante lembrar que, alem de não temos valores duplicados não temos ordem

lista = [99, 2, 34, 23, 2, 12, 1, 44, 5]
print(f'Lista : {lista} com {len(lista)}')

tupla = (99, 2, 34, 23, 2, 12, 1, 44, 5)
print(f'tupla: {tupla}  com {len(tupla)}')

dicionario = {}.fromkeys(lista, 'dict')
print(f'Dicionário: {dicionario} com {len(dicionario)}')

conjunto = {99, 2, 34, 23, 2, 12, 1, 44, 5}
print(f'Conjunto: {conjunto} com {len(conjunto)}')


# Podemos colocar qualquer tipo de dados em um set
s = {1, 'b', True, 34.22, 44}
print(type(s))
print(s)

# Podemos Iterar em um set
for valor in s:
    print(valor)

# Uso Interessante com sets
# Imagine que fizemos um formulário de cadastro de visitante em uma feira ou museu
# Os visitantes informam manualmente a cidade de onde vieram
# Nós adicionamos cada cidade em uma lista Python, ja que em uma lista podemos ter repetição

cidades = ['Belo Horizonte', 'São Paulo', 'Campo Grande', 'Cuiabá', 'Campo Grande', 'São Paulo', 'Cuiabá']

print(cidades)
print(len(cidades))

# Precisamos saber quantas cidade distintas, ou seja unicas, temos.
# Oque vc faria?
print(len(set(cidades)))

# Adicionando um elemento em um set (Conjunto)
s = {1, 2, 3}
s.add(4)
s.add(4)  # Duplicidade não gera erro, simplesmente não é adicionado ao set
print(s)


# Remover um elemento em um conjunto
s = {1, 2, 3}
print(s)

# Forma 1
s.remove(3)  # Aqui esta removendo o valor e não indece 3
print(s)


# Caso tente remover um valor que não exista, vai gerar um KeyError
# s.remove(33)  # Não é indece que esta tentando remover aqui é Valor, e não foi encontradao e gerou KeyError,
# nenhum valor  retornado

# Forma 2
s.discard(2)
print(s)
# No discard se o valor não é encontrado não gera nenhum erro

s = {1, 2, 3}
print(s)


# Copiando um conjunto para outro ...
# Forma 1 - Deep copy - cria uma cópia independente
novo = s.copy()
print(novo)

novo.add(4)
print(s)
print(novo)

# Forma 2 - Shallow Copy - Estão apontando pra o mesmo espaço em memoria
novo = s
novo.add(4)
print(s)


# Podemos remover todos os itens de um conjunto
s.clear()
print(s)

# Métodos Matematicos de juntos

# Imagine que temos dois conjuntos: Um contendo estudantes do curso de Python e um
# contendo estudantes de curso de Java.


estudantes_python = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patricia'}

# Veja que alguns alunos que estudam python também estudan Java

# Precisamos gerar um conjunto com nome de estudantes unicos
# Forma 1 - utilizando union
unicos1 = estudantes_python.union(estudantes_java)
print(unicos1)

# Forma 2 - utilizando o caractere pipe |
unicos2 = estudantes_python | estudantes_java
print(unicos2)

# Gerar um conjunto de estudantes que estão em ambos os cursos
# Forma 1 - utilizando o intersection
ambos1 = estudantes_python.intersection(estudantes_java)
print(ambos1)

# Forma 2 - Utilizando o &
ambos2 = estudantes_python & estudantes_java
print(ambos2)

# Gerar um conjunto de estudantes de um curso qu não estão no outro
so_python = estudantes_python.difference(estudantes_java)
print(so_python)

so_java = estudantes_java.difference(estudantes_python)
print(so_java)


# Soma, Maior valor, Menor, tamanho
# * Se os valores forem numeres inteiros ou reais

s = {1, 2, 2, 3, 4, 5}
print(s)
print(max(s))  # Imprimindo maior valor do conjunto
print(min(s))  # imprimindo menor valor do conjunto
print(sum(s))
print(len(s))

