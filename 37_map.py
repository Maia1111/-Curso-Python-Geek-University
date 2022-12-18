"""
Map 

Com map, fazemos mapeamento de valores para função.

"""
import math


def area(r):
    """
    calcula area de um circulo com raio 'r'.
    """
    return math.pi * (r ** 2)


# Testando a função
print(area(2))
print(area(5.3))


# Forma comum de mapear uma lista pra uma função
raios = [2, 5, 7.1, 0.3, 10, 44]

areas = []
for raio in raios:
    areas.append(area(raio))


print(areas)    


# Mapeando utilizando map
# Map é uma função que recebe dois parâmetros: o primeiro a função, o segundo um iterável

areas = map(area, raios)
print(type(areas))
print(area)  # imprimindo direto sem converter pra lista - retorna um objeto map
print(list(areas))  # Aqui convertendo pra lista e retornando uma lista

# Outra forma utilizando Lambda
# Map com Lambda

print(list(map(lambda r: math.pi * (r ** 2), raios)))
