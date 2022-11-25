"""
Loop é estrutura de repetição

Python
for item in interavel:
    //execução do loop

Utilizamos loops para iterar sobre sequências ou valores iteráveis.

São alguns exemplos de iteráveis
    - String
    - Listas
    - Range
"""
nome = 'Geek university'
lista = [1, 2, 3, 5, 7, 9]
numeros = range(1, 10)

# exemplo de for 1
# Iterando sobre uma String
for letra in nome:
    print(letra)

# iterando sobre uma lista
for numero in lista:
    print(numero)


# Iterando sobre um range
for i in range(0, 10):
    print(i)

# imprimindo o indice junto com o valor utilizando enumerate
for indece, letra in enumerate(nome):
    print(indece, letra)

soma = 0

qtd = int(input('Quantas vezes o loop vai rodas? '))
for i in range(1, qtd+1):
    num = int(input(f"Digite um numero {i}/{qtd} :"))
    soma = soma + num
print(f'A soma é {soma}')


# Mudando o separador do for ( por padrão pula uma linha)
# Se vc quizer outro comportamento tem que colocar outro separador
for i in nome:
    print(i, end='')
# &#128512
print()
for num in range(1, 11):
    print(f'\U0001F60D' * num)
