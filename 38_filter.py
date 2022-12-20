"""
Filter 


filte() -> server para filtrar dados de uma determinada coleção.



 
valores = 1, 2, 3, 4, 5, 6


media = (sum(valores) / len(valores))
print(media)
 
 """
 
 
import statistics   # Biblioteca para trabalhar com dados estatísticos



# Dados coletados de algum sensor 
dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# Calculando a média dos dados utilizando a função mean()

media = statistics.mean(dados)
print(media)

# OBS: assim como a função map(), a filter() recebe dois parâmetros, sendo uma função é um iteravel 

res = filter(lambda valor : valor > media, dados)
print(list(res))   # apos utilizar a primeira vez os dados são apagados
print(type(res))

print(f'novamente: {list(res)}')  # tentanto exibir aqui novamente, mais ja foi zerado os dados


# OBS: Assim  como a função map(), o filter() após pela primeira vez serem utlizados os dados eles
# são excluidos da memoria



"""
    Uma outra utilização do filter() é remoção de dados faltantes 
    Acompanhe o exemplo abaixo. 
    
"""

# Lista com dados faltantes
paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colombia', '', 'Equador', '', '', 'Venezuela']

# imprimindo a lista com dados faltantes
print(paises)


# Fazendo filtro retirando dados faltantes
# None no filter vai fazer com que seja retirado os dados em branco
res = filter(None, paises)
print(list(res))

"""
    A diferença entre map e filter() é :
    
       - map() -> Recebe dois parâmetros, uma função e um iterável, e retorna todos os valores  do 
                  iteráverl mapeando para a função.
       
       filter() -> Recebe dos parâmetros, uma função é um iterável, porém, retorna os elementos 
                   de acordo com a função propos, podemos dizer que a função filter retorna True ou False.
       
"""


# Exemplo mais complexo

usuarios = [
    {"username":"samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizza"]},
    {"username":"Carla", "tweets": ["Eu amo gato"]},
    {"username":"jeff", "tweets": []},
    {"username":"bob123", "tweets": []},
    {"username":"doggo", "tweets": ["Eu gosto de cachorro", "Eu vou sair hoje"]},
    {"username":"gal", "tweets": []}
]

# filtrar os usuários que estão inativos no Twitter
# imprimindo a lista pra observar como fica sem fazer nada
print(usuarios)


# Utilizando filter pra trazer todos os usuários que estão com lista de twitter vazias

# Forma 1 
inativos = list(filter(lambda usuario: len(usuario['tweets']) == 0, usuarios))
print('Usuários inativos')
# Trazendo a lista completa
print(inativos)


# Forma 2 
inativos = list(filter(lambda usuario: not usuario['tweets'], usuarios))
print(inativos)

