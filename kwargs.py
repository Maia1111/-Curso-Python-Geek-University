"""
**kwargs 

Poderiammos chamar esse parâmetros  de **xis, mais por convençao chamamos de **kwargs


Este é só mais uma parâmetro, mais diferente de *args que coloca os valores extras
em uma tupla, o **kwargs exige que utilizemos parâmetros nomeados, e transforma esses 
parâmetros extras em um dicionário.


"""


# Exemplo 
def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa.title()} é {cor}')
    

cores_favoritas(mrcos='verde', julia='Amarelo', fernanda='azul', vanessa='branco')


cores_favoritas()


# OBS: Os parâmetros *args e **kwargs não são obrigatórios.




def cumprimento_especial(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == 'Python':
        print('Você recebeu um cumplimento Pythônico Geek')        
    elif 'Geek' in kwargs:
        return f"{kwargs['geek']} Geek"
    return 'Não tenho certeza quem vc é .....'


print(cumprimento_especial())
print(cumprimento_especial(geek='Python'))
print(cumprimento_especial(geek='oi'))
print(cumprimento_especial(geek='especial'))


"""
Em nossas funções, podemos ter os argumentos nesta ordem
   - Parâmetros obrigátórios
   - *args  (Vira uma tupla com os valores passados)
   - Parametros Padrão (default) - com valores já iniciados
   - **kwargs (dicionário)
"""

# Exemplo

def  minha_funcao(idade, nome, *args, solteiro=False, **kwargs):
    print(f'{nome} tem {idade} anos')
    print(args)
    if solteiro:
        print('solteiro')
    else:
        print('casado')
    print(kwargs)
    
    

minha_funcao(40, 'Rogério')
minha_funcao(18, 'Felicity', 4, 5, 3 , solteiro=True)
minha_funcao(30, 'felipe', vai='não', voce='vai')
minha_funcao(19, 'Carla', 9, 4, 3, java=False, python=True)



# Função com todos os tipo de parâmetros em ordem correta
def mostra(a, b, *args, instrutor='Geek', **kwargs):
    return [a, b, args, instrutor, kwargs]   # retorna a lista de todos os parâmetros



print(mostra(1, 2, 3, sobrenome='University', cargo='Instrutor'))

"""
a = 1
b = 2
args = (3,)
instrutor = 'Geek'
kwargs = {'sobrenome': 'University', 'cargo': 'instrutor'}
"""



# Exemplo de função que pode ser desempacotada 
def mostra_nomes(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"


nomes = {'nome': 'Felicity' , 'sobrenome':'Jones'}

# usa-se o duplo asterisco para desempacotar o argumento de dicionário que recebemos
print(mostra_nomes(**nomes))



def soma_multiplos_numeros(a, b, c):
    print(a + b + c)
    

lista = [1, 2, 3]
tupla = (1, 2, 3)
conjunto = {1, 2, 3}
dicionario = dict(a=1, b=2, c=3)

soma_multiplos_numeros(*lista)
soma_multiplos_numeros(*tupla)
soma_multiplos_numeros(*conjunto)
soma_multiplos_numeros(**dicionario)

# OBS! Os nomes da chave em um dicionário deve ser os mesmos que dos parâmetros da função

# dicionario = dict(d=1, e=2, f=3)     # Vai gerar um TypeError por que os parâmetros do dicionário são escritos 
# diferentes dos parâmetros das funções

