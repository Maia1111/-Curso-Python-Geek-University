"""
Módulo Collections - Counter ( Contador)
Collections -> High performance Container Datetypes

Counter -> Recebe um iteravel como parâmetro e cria um objeto do tipo Collections Counter que é parecdido
como um dicionário, contendo como chave o elemento  da lista que passada como parâmetro9  e como valor
a quantidade de ocorrencias deste elemento.


"""

# Realizado o import
from collections import Counter

# podemos utilizar qualquer iterável, aqui usamos a lista
lista = [1, 1, 2, 2, 3, 3, 3, 3, 4, 4, 4, 5, 6, 45, 45, 66, 66, 43, 34]

# Utilizando o Counter
res = Counter(lista)
print(type(res))
print(res)

#  Counter({3: 4, 4: 3, 1: 2, 2: 2, 45: 2, 66: 2, 5: 1, 6: 1, 43: 1, 34: 1})
#  Veja  que para cada elemento da lista o Counter criou uma chave e colocou como valor a quantida de ocorrências


# Ele pode pegar e fazer um Counter direto de uma string
print('Fazendo Counter da string "Geek university"')
print(Counter('Geek university'))
# Counter({'e': 3, 'i': 2, 'G': 1, 'k': 1, ' ': 1, 'u': 1, 'n': 1, 'v': 1, 'r': 1, 's': 1, 't': 1, 'y': 1})


# Exemplo 3

texto = """
A habilidade de escrever bem acaba sendo, em muitos setores da vida, essencial. Ainda mais quando se trata de 
vestibular.

Alguns dos principais exames do país, como Enem e Fuvest, exigem que seus candidatos desenvolvam uma redação no formato 
dissertativo-argumentativo, que consiste em apresentar seu ponto de vista sobre determinado tema, e defendê-lo com a
rgumentos consistentes.

Se você busca ajuda, e sobretudo, dicas de como escrever uma redação perfeita e alavancar na disputa por uma vaga na
universidade, vem com a gente. Neste artigo você vai saber tudo sobre o texto dissertativo-argumentativo e
 como estruturá-lo. Boa leitura!
"""
# Primeiro vc gera uma lista de palavras com o split do texto
palavras = texto.split()

# Aqui aplica o Copunter na lista de palavras
res = Counter(palavras)
print(res)

# Pegando as 5 palavras com mais ocorrencias no texto
print(res.most_common(5))
