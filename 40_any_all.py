"""
Any e All 

São duas funções integradas do Python.


all() -> Retorna True  se todos os elementos do iterável são verdadeiros ou se 
ainda se o iterável esta vazio.

"""

# Exemplo all()
print(all([0, 1, 2, 3, 4])) # Todos os números são verdadeiros?

# Só retorna se todos os elementos for True, mais o zero é false 

print(all([ 1, 2, 3, 4])) #  Aqui retornará True, porque todos elementos são True.

print(all([]))  # Retorna True se o iterável for vazio


# Outra utilização com listcomprehension
nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina']

print(all([nome[0] == 'C' for nome in nomes]))  # Busca pra mim se todos nomes na inicial começa com 'C'
# Retornará True, por que todos os nomes começam com 'C'.

# Outro Exemplo
print(all([num for num in [2, 4, 6, 8] if num % 2 == 0])) # Vai retornar True por que todos elementos 
# são par




# função any() - Significa algum  for verdadeira já retorna True
print(any([1, 2, 3, 4]))  # retorna True

print(any([0, [], {}])) # retorna False, porque todos os elementos são False


