"""
Set Comprehension 

Lista = [1, 2, 3, 4, 5]

set = {1, 2, 3, 4, 5}

"""
# Exemplos
numeros = {num for num in range(1, 7)}
print(numeros)

numeros = {x * 2 for x in range(1, 11)}
print(numeros)


# Gerando um dicionário
dicionario = {x:(x * 2) for x in range(10)}
print(dicionario)



# Pra finalizar
letras = {letra for letra in 'Geek University'}

print(letras)