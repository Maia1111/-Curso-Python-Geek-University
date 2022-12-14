"""
Funções com parâmetros (de entrada)

- Funções que recebem dados para serem processados dentro da mesma


Se a gente penser em um programa qualquer, geralmente temos:

Entrada -> Prodecessamenteo -> saída

Se agente pensar em uma função, já sabemos que temos funções que:
- Não possuem entrada;
- Não Possuem saída;
- Possuem entrada mais não possuem saída;
- Não possuem entrada mais possuem saida;
- Possuem entrada e saida
"""

# Refatorando uma função

def quadrado(numero):
    return numero ** 2

print(quadrado(7))
print(quadrado(2))
print(quadrado(5))

# funçõe podem ter n parâmetros Necessários
def soma(a, b):
    return  a + b



def multiplica(num1, num2):
    return num1 * num2


def outra(num1, b, msg):
          return(num1 +b) * msg



print(soma(2, 5))
print(multiplica(10, 20))
print(outra(1, 2, 'Geek '))

# OBS: se agente informa um número errado de parâmetro ou argumanto, Teremos TypeError


# Nomeando parâmetros
def nome_completo(nome, sobrenome):
    return f'Seu nome completo é {nome} {sobrenome}'


print(nome_completo('Rogério', 'Maia'))


# Diferença de Parâmetros e argumentos
# Parametros são variáveis declaradas na definição de uma função;
# Argumentos são dados passados relativos aos argumentos da função;


#  A Ordem dos parâmetos importam

# Argumentos nomeados (Keyword Arguments)

"""
Caso utilizaremos nomes dos parâmetos nos argumentos para informa-los, 
podemos utilizar qualquer ordem

"""
print(nome_completo(nome='Rogério', sobrenome='Maia'))


# Imprimindo em ordem diferente mais com os argumentos nomeados
print(nome_completo(sobrenome='Maia', nome='Rogério'))
print(nome_completo(sobrenome='Silva', nome='Marcia'))


# Erro comum na utilização do return

"""
Forma errada com return dentro do for - o return já encerra a função no primeiro loop


Exemlo errado

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total += num
        return total

"""
# Exemoplo certo com return fora do bloco do for
def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total += num
    return total


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(soma_impares(lista))
