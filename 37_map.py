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


# Forma comum de mapear uma lista pra uma função sem função map
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


# OBS: Após utilizar a função map() deposis da primeira utilização do resultadao, ele zera.
# todo objeto map retorna um iterável 



# para fixar - Map
# Temos dados iteráveis



# Mais exemplos
cidades = [('Berlim', 29 ), ('Cairo', 36), ('Buenos Aires', 19), ('Los Angeles', 26), ('Tokio', 27), ('Nova Youk', 28), 
           ('Londres', 22)]

print(cidades)


# Transformar as temperaturas das cidades em Firenait utilizando map

# formula  -  f = 9/5 * graus_celcius + 32 

# Lambda 
c_para_f = lambda dado :(dado[0], 9 / 5 * dado[1] + 32)

# 
print(list(map(c_para_f, cidades)))