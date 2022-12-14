"""
Módulo Collections - Default Dict

# Relembrando dicionário comum
dicionario = {'curso': 'Programação em Python: Essencial'}
print(dicionario)
print(dicionario['curso'])
print(dicionario['outro'])  # Dicionario comum gera erro KeyError


Ao criar um dicionário utilizando-o, nos informamos uym valor default,
podemos utilizar um lambda para isso. Este valor será utilizado sempre que não houver um
valor definido. Caso tentemos acessar  que não existe, essa chave será criada e o valor
default será atribuído.

OBS: Lambdas são funções anonimas que podem receber ou não parametros e retornar valores
"""
# Fazendo import do defaultdict
from collections import defaultdict

dicionario = defaultdict(lambda: 0)
dicionario['curso'] = 'Programação em Python: Essencial'
print(dicionario)

# Aqui ele retorna o valor 0, mais já cria a chave outro com valor padrão 0
print(dicionario['outro'])

# Aqui ele já mostra o elemento novo criado
print(dicionario)




