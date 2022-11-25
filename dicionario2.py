"""
Mapas -> Conhecidos em Python como dicionários

Dicionários em Python são representados por chaves {}7
"""

receita = {'jan': 100, 'fev': 250, 'mar': 400}

# Imprimindo dicionario
print(receita)

# Iterar sobre dicionário

# Trazendo somente as chaves
for chave in receita:
    print(chave)

# Trazendo os valores
for chave in receita:
    print(receita[chave])

# Trazendo chave e valor de forma mais incrementada
for chave in receita:
    print(f'Em {chave}: recebi  R${receita[chave]}')

# Imprimindo somente as chaves - modo Pythônico
print(receita.keys())

# Iterando somente nas chaves - modo Pythônico
for chave in receita.keys():
    print(chave)

# Imprimindo somente valores
print(receita.values())

# Iterando somente nos valores
for valor in receita.values():
    print(valor)


# Desempacotamento de dicionário
print(receita.items())  # devolve lista de tuplas das chaves e valores

for chave, valor in receita.items():
    print(chave, valor)

# Podemos encontar valor máximo, valor minino, tamanho
print(min(receita.values()))
print(max(receita.values()))
print(sum(receita.values()))
print(len(receita))

# OBs: Para somar, encontrar o valor maximo e valor mínimo os valores precisam ser inteiros ou números reais
