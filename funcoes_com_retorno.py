"""
Funções com Retorno

numeros = [1, 2, 3]

ret = numeros.pop()
print(f'Retorno de pop {ret}')

ret_pr =  print(numeros)
print(ret_pr)

Em Python quando uma função não retorna nenhum valor, o retorno é none

OBS: Funções Python que retornam valores devem utilizar a palavra reservada return
1 - O return  finaliza a função
2 - podemos ter ema um função diferentes returns;
3 - Podemos, em uma função, retornar qualquer tipo de dado e até mesmo multiplos valores;
def quadrado_de_7():
    return 7 * 7


ret = quadrado_de_7()

print(f'Retorno de ret {ret}')

# Refactorando a primeiro função que fizemos


def diz_oi():
    print('Estou sendo executado antes do return')
    return 'Oi!'
    print('Estou sendo executado  depois  do return')


alguem = 'Pedro'

print(diz_oi() + alguem)



Exemplo 2

def nova_funcao():
    variavel = False
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    else:
        return 'b'

print(nova_funcao())
"""
from random import random


def outra_funcao():
    return 1, 2, 3, 4


num1, num2, num3, num4 = outra_funcao()
print(num1, num2, num3, num4)


# Vamos criar uma função para jogar moedas

def joga_moeda():
    # Gera um numero randomico entre 0 e 1
    valor = random()
    if valor > 0.5:
        return 'Cara'
    else:
        return 'Coroa'


print(joga_moeda())
