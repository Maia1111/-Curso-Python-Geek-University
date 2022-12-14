
"""
Dicionários

OBS: em Algumas linguagens de programação os dicionários são conhecidos
por mapas.


Dicionários são coleções do tipo com chave/valor

Dicionário são representados por chaves {}
print(type({}))
OBS: sobre dicionários
     - Chave e valor são separados por dois pontos
     - Tanto chave quanto valor podem ser de qualquer tipo de dado
     - Podemos misturar tipos de dados


Tipo None
O tipo  de dado None em Python representa um tipo sem tipo, ou poderia ser conhecido tmabme como
tipo vazio, porém, falar que um tipo sem tipo é mais apropriado.

OBS o tipo Nome é sempre especificado com a primeira letra maiscula.

OBS: O Tipo None sempre será False
"""

# Criação de Dicionário

# forma 1 - Mais comum
paises = {'br': 'brasil', 'eua': 'Estados unidos', 'py': 'Paraguai'}

print(paises)
print(type(paises))

# Forma 2 (menos comum)
paises = dict(br='Brasil', eua='Estados unidos', py='Paraguay')

# Acessando elementos de um dicionário
# Dicionário não são indexados automaticamente - se faz o acesso pela chave

# Acessando elementos
# forma 1 - Acessando pela chave
print(paises['br'])
print(paises['py'])

# OBS Caso tentamos fazer um acesso utilizando uma chave que não existe teremos KeyError

# Forma 2 - Acessando a utilizar o get (RECOMENDADA)
# Utilizando get não gera erro caso a chave utilizada não exista
print(paises.get('br'))
print(paises.get('ru'))

paises = {'br': 'brasil', 'eua': 'Estados unidos', 'py': 'Paraguai'}

russia = paises.get('py')
pais = paises.get('py')
if russia:
    print(f'Encontrei o país {pais}')
else:
    print('Não encontrei o país')

# Utilizando get eu posso ainda definir um valor padrão caso não encontre
pais = paises.get('ru', 'Não encontrado')
print(pais)

paises = {'br': 'brasil', 'eua': 'Estados unidos', 'py': 'Paraguay'}

# Verificando se determinada chave se encontram em um diciionário
print('br' in paises)
print('ru' in paises)
print('Estados unidos' in paises)
print('Paraguay' in paises)


# Podemos utilizar qualquer tipo de dado (int, float, string, bolean) inclusive lista, tupla, dicionário, como chave

# Tuplas são Bastante interessante para serem utilizadas como chaves de dicionários pois são imutavéis.
localidades = {
    (35.6895, 39.6917): 'Escritório em Tokio',
    (40.7128, 74.0060): 'Escritório em Nova Yourk',
    (35.6895, 39.4000): 'Escritório em Tokio'
}

print(localidades)
print(type(localidades))

# Adicionar elementos em dicionário
receita = {'jan': 100, 'fev': 120, 'mar': 300}
print(receita)
print(type(receita))

# Forma 1 - mais comum
receita['abr'] = 350
print(receita)

# Forma 2
novo_dado = {'mai': 500}
receita.update(novo_dado)
print(receita)

# Atulizando dados em um dicionário
# Forma 1

receita['mai'] = 500
print(receita)

# Forma 2
receita.update({'mai': 600})
print(receita)

# Conclusão 1 : A forma de adicionar novos elementos ou atualizar dados em um dicionário é a mesma
# Conclusão 2 : Em dicionários, Não podemos ter chaves repetidas

# Remover dados de um dicionário

receita = {'jan': 100, 'fev': 120, 'mar': 300}

# Forma 1 - Mais comum
ret = receita.pop('mar')
print(ret)
print(receita)
# OBS : Aqui precimos SEMPRE  informar a chave, e caso não encontre o elemento, um KeyError é retornado
# OBS:  Ao removermos um objeto , o valor deste objeto é sempre retornado

# Forma 2

del receita['fev']
print(receita)

# Se a chace não exitir será gerado um KeyError
# OBS Neste caso o valor é removido mais não é retornado

# Imagina que vc tem um comercio eletrêonico , onde teremos um carrinho de compras na qual adicionamos produdutos
"""
Carrinho de compras:
    Produto 1:
        - nome;
        - quantidade;
        - preço
    Produto 2:
        - nome 
        - quantidade;
        - preço 
    
"""

# - Poderiamos utilizar uma lista para isso ? Sim
carrinho = []

produto1 = ['Playstatio', 1, 230.00]
produto2 = ['Gold Of War', 1, 150.00]

carrinho.append(produto1)
carrinho.append(produto2)
print(carrinho)

produto1 = {'nome': 'Playstation', 'quantidade': 1, 'preço': 2300.00}
produto2 = {'nome': 'God of War', 'quantidade': 1, 'preço': 150.00}


carrinho2 = []

carrinho2.append(produto1)
carrinho2.append(produto2)
print(carrinho2)

# Metodos de um dicionários

d = dict(a=1, b=2, c=3)
print(d)
print(type(d))

"""
# Limpar dicionário(Zerar dados)
d.clear()
print(d)

"""

# Forma não usual de criação de dicionários

usurio = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido')
print(usurio)
print(type(usurio))


# O Método fromkeys recebe dois parâmetros: um iterável e um valor
# Ele vai gerar para cada valor do iterável uma chave e irá atribuir a esta chave o valor informado no segundo parêmetro

veja = {}.fromkeys('teste', 'valor')
print(veja)

veja = {}.fromkeys(range(1, 11), 'novo')
print(veja)

