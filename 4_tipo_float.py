"""
Tipo float

Tipo real, decimal,
numeros com casas decimais

OBS: O separador de casas decimais na programação é o ponto e não a virgula


"""

# errado do ponto de vista do float
valor = 1, 44   # Ele entende que é uma tupla quando coloca a virgula ao invés de ponto
print(valor)

# Certo do ponto de vista do float
valor = 1.44
print(valor)

# É possivel fazer uma tupla de atriubuição
valor1, valor2 = 1, 44
print(type(valor1))
print(type(valor2))
print(valor1)
print(valor2)

# Podemos converte Float em int

"""
Ao converter valores float para inteiros, nós perdemos precisão

"""
res = valor
print(res)
print(int(valor))

