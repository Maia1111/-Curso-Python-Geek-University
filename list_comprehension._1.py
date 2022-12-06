"""
List Comprehension


- utilizando List Comprehension nśo podemos gerar novas listas com dados processados apartir 
de outro iterável.


# sintaxe da lista Compreension

[dado for dado  in iterável]



"""

#  Exemplos

numeros = [1, 2, 3, 4, 5]

res = [numero * 10 for numero in numeros ]

print(res)


"""
Para entender melhor oque esta acontecendo  devemor dividir a expressão em duas partes :

Primeira expressão que vai fazer com cada valor do iteravel 
Segunda parte um iteravel que vai ser processado cada um dos seus valores

"""

# Comprehension versos Loop 
numeros = [1, 2, 3, 5]
numero_dobrado = []

# Utilizando Loop
for numero in numeros:
    numero =  numero * 2
    numero_dobrado.append(numero)    
print(numero_dobrado)


# Utilizando List Comprehension 
res = [numero * 2 for numero in numeros]
print(res)


# Outros exemplos

# 1
nome = 'Geek University'
print([letra.upper() for  letra in nome])

# 2 
amigos = ['maria', 'julia', 'pedro', 'guilherme' , 'vanessa' ]
print([nome.title() for nome in amigos])


# 3 
print([numero * 3  for numero in range(1, 10)])


# 4
print([bool(valor) for valor in [0, [], '', True, 1, 3.14]])
