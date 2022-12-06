"""

List Comprehension

Nos podemos adicionar estruturas condicionais lógicas as nossas list Comprehension


"""

# Exemplos

# 1
# usar condicionais pra gerar uma lista somente com os pares apartir de uma lista
numeros = [1, 2, 3, 4, 5, 6]

pares = [numero for numero in numeros if numero % 2 == 0 ]
impares = [numero for numero in numeros if numero % 2 != 0]
print(pares)
print(impares)


# Refator 
# Qualquer número par módulo de 2 é 0 e zero em Python é False. not False = True
pares = [numero for numero in numeros if not numero % 2]
impares = [numero for numero in numeros if  numero % 2]
print(pares)
print(impares)

# Exemplo com else
res = [numero * 2 if numero % 2 == 0 else numero / 2 for numero in numeros]
print(res)