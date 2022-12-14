"""
Definindo Funções
  - Funções são pequenas partes  de codigos que realizam tarefas específicas;
  - Uma função pode ou receber entradas de dados  e retornar uma saída de dados;
  - Muitos uteis para executar procedimentos silimilares por repetidas vezes;

OBS:  Se você escrever uma função  que realiza várias tarefas dentro dela, é bom
verificar se não há possibilidade de simplifica-la, Procure fazer  funções simples.


  Já utlizamos varias funções desde que iniciamos este curso:
      - print()
      -len()
      - max()
      - min()
      - count()
      - e muitas outras;
"""

# Exemplo de utilização de funções
cores = ['verde', 'amarelo', 'azul', 'branco']

# Utilizando a função integrada (Built-in) do Python - Toda função que ja vem com Python é chamada de Bult-in
print(cores)

curso = 'Programação em Python: Essencial'
print(curso)


# Repare que a função ela não quer saber o tipo de dado, ele executa a função de printar no console

cores.append('roxo')
print(cores)

# As funções são parte do princípio DRY - não repita você mesmo ou náo repita código

# COMO DEFINIR FUNÇÕES
"""
Em Python, a forma geral de definir uma função é:

def nome_da_funcao(parametro_de_entrada):
   bloco_da_funcao
   
   

Onde:
   - nome_da_funcao -> SEMPRE, com letras minúsculas, e se for nome composto, separado por underline(Snake Case)
   - parametros_de_entrada -> são opcionais, onde temos mais de um, casa um é separado por vírgula, podendo ser opcional
     ou não.
   - bloco_da_funcao -> Também chamamos de corpo da funcão ou implementação, é onde o processamento da função acontece
     no bloco pode ter ou não retorno
   """

# Definindo


def diz_oi():
    print('oi')


"""
OBS: 

1 - Veja que, dentro das funcões podemos utilizar outras funções;
2 - Veja que, nossa função só executa uma tarega, unica coisa que ela faz é diz oi;
3 - Veja que, esta função ela não recebe nenhum parâmetro de entrada;
4 - Veja que esta função não retorna nada;

"""

# importante
# Lembre que a função só é executa com parênteses
diz_oi()
"""
Nunca esqueça de utilizar os parênteses ao utilizar uma função


# Errado 
diz_oi 

# certo 
diz_oi()


# Errado

"""


def cantar_parabens():
    print('Parabéns pra você')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('Viva o aniversariante!')


cantar_parabens()
cantar_parabens()
cantar_parabens()
cantar_parabens()

# Executando a função dentro de um for
for n in range(5):
    cantar_parabens()

# Python podemos criar uma variavel e atribuir uma função a essa variável e depois executar a variável como função
print('\nMostrando a variavel como funçã́o')

# não comum
cantar = cantar_parabens
cantar()


