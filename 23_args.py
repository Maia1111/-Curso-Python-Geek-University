"""
Entendendco o *args 

- O *args é um parâmetro, com outro qualquer. Isso significa que você poderá
chamar de qualquer coisa, desde que começe com asterisco.

Exemplo:
*xis

Mais por convençao, utilizamos *args para defini-los

Mais oque é o *args?
O parâmetro  *args utilizado em função, coloca os valores extras informados como entrada 
em uma tupla. Então desde já lembre-se  que tuplas são imutáveis.

"""

# Exemplo 
def soma_todos_numeros(num1, num2, num3):
    return num1 + num2 + num3


print(soma_todos_numeros(1, 2, 3))

# print(soma_todos_numeros(6, 4))   # Aqui teremos  um TypeError - A função espera receber 3 argumentos
# print(soma_todos_numeros(1, 2, 4, 5))  # Aqui estou passando mais parâmetros que a função pede



# Entendeno o *args


def soma_todos_numeros2(*args):
      return sum(args)  # para utilizar escreve somente args


print(soma_todos_numeros2())
print(soma_todos_numeros2(1))
print(soma_todos_numeros2(2, 3))
print(soma_todos_numeros2(2, 3, 4))


# outro exemplo utilização

def verifica_info(*args):
    if 'Geek' in args and 'University' in args:
        return 'Bem vindo a Geek!'
    return 'Eu não sei quem vc é!'


print(verifica_info())
print(verifica_info(1, True,'University', 'Geek'))
print(verifica_info(1, 'University', 3.145))


# quando passamos uma lista no args - precisamos desempacotar
# Exemplo

numeros = [1, 2, 3, 4, 5, 6, 7]

# Se passarmos de forma simples a lista como parâmetro de um args vai dar erro
"""
Exemplo com erro

def soma_todos_numeros(*args):
    return sum(args)
    
    
print(numeros)  -> vai gerar um erro, por que ele vai armazenar a lista em uma tupla e a função 
não vai conseguir realizar a operação.

Para resolver, teremos que desempacotar a lista na tupla


    """
# Desempacotador

print(soma_todos_numeros2(*numeros))  # Colocando um asterisco no argumento da lista que esta passando

# O asterisco serve para informamos ao Python que estamos passando uma coleção como argumento
# Desta forma ele sabera que precisara desempacotar os dados

# NÃO FUNCIONA COM DICIONÁRIO