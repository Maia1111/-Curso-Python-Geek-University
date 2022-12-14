"""

Utilizndo Lambdas

Conhecidas com expressões lambdas, ou simplesmente Lambdas, são funções sem nome, ou seja, 
funções anônimas.


# Função em Python 

def soma(a, b):
    return a + b

"""

# Exemplos de Função em Python


def funcao(x):
    return 3 * x + 1


print(funcao(4))

# Exemplo de expressão Lambda


#  E como utlizar a expressão lambda
def calc(x): return x * 3 + 1


print(calc(4))


# Podemos ter expressão lambdas com multiplas entradas.

def nome_completo(nome, sobrenome): return nome.strip(
).title() + ' ' + sobrenome.strip().title()


print(nome_completo('ROGERIO', 'Maia'))


# Em funções Python podemos ter nenhuma ou várias entradas. Em funções lambdas também

# Lambda sem entrada
def amar(): return 'Como não amar python'


def uma(x): return 3 * x + 1
def duas(x, y): return (x * y) ** 0.5
def tres(x, y, z): return 3 / (1 / x + 1 / y + 1 / z)


print(amar())
print(uma(6))


# Outro exemplo
autores = ['Isaac Asimov', 'Ray Braubury', 'Robert Heinlein', 'Arthur C. Clarke', 'Frank Herbert', 'Orson Scott Card',
           'Douglas Adams', 'H. g. Wells', 'Leig Bracket']

print(autores)
autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())

print(autores)