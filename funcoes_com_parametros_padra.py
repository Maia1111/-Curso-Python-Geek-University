"""
Funções com Parâmetros padrão(default parameters)


funções onde a passagem de parâmetos seja opcional


Exemplo de função onde o parâmetoé opcional

# Repare que aqui informamos um argumento pra função print
print('Geek university')

# Aqui não infomamos nenhum, mesmo assim não é reclamado nenhum erro
print()


Por que utilizar parâmetros defautl ?
   - Nos permite ser mais flexíveis nas funções
   - Evita Erros com parâmetros incorretos 
   - Nos permite trabalhar com exemplos mais legiveis de códigos

Qual tipo de dados podemos utilizar como valores de dados default:
   - Qualquer tipo de daos:
        Números, strings , floats, booleanos, listas, tuplas, dicionários, funções e etc.
        


"""

def expo(numero, potencia=2):
    return numero ** potencia


print(expo(2))


# Exemplo mais complexo de parametros nomeados

def mostra_informacao(nome='Geek', instrutor=False):
    if nome == 'Geek' and instrutor:
        return f'Bem vindo  instrutor a Geek'
    elif nome == 'Geek':
        return 'Eu pensei que era o instrutor'
    return f'Olá {nome}'

print(mostra_informacao())
print(mostra_informacao(instrutor=True))
print(mostra_informacao('Rogério'))


# Exemplos de funções recebendo como parãmetros outras funções
def soma(num1, num2):
    return num1 + num2


def mat(num1, num2, fun=soma):
    return fun(num1,num2 )


def subtracao(num1, num2):
    return num1 - num2

print(mat(2, 3))
print(mat(3, 2, subtracao))


# Escopo - Evitar problemas e confusões
# Variaveis Globais
# Se tivermos uma variavel local com mesmo nome de uma variável local, a variável local tera preferencia.
# Variável locais só são reconhecida dentro do bloco onde foram declaradas.
# ATENÇÂO com variáveis globais (se puder evitar, evite!), caso utilize fique atento aos escopos.


instrutor = 'Geek'  # Variáveis Globais

def diz_oi():
    instrutor = 'Python'   # Varivavel local do bloco se cobrepõe a variavel global
    return f'Oi {instrutor}'

print(diz_oi())

 # Exemplo de utilização de variáveis globais em função
 
total = 0  # Variável global


def incrementa():
    global total  # avisando pro python que esta utilizando variável global
    total = total + 1  # se for fazer calculo com variáveis globais sempre declare ela no inicio como global
    return total

incrementa()
incrementa()
incrementa()
incrementa()

 
 
 # Não muito comum
 