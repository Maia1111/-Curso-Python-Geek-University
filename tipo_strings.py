"""
Tipo Strings

Em Python um tipo é considerado String sempre que:

- Estiver entre àspas simpples -> 'uma string', 'a', 'True', '42.3'
- Estiver entre àspas duplas -> "uma string", "a", "True", "42.3"
- Estiver entre àspas simples triplas -> '''uma string''', '''a''', '''True''',  '''42.3'''


"""
# - Estiver entre àspas duplas triplas ->"""uma string""", """a""", """True""",  """42.3"""

nome = 'Geek University'
print(nome)
print(type(nome))

nome = " Gina's Bar"
print(nome)
print(type(nome))

nome = """Angelina 
Jolie
"""
print(nome)
print(type(nome))


nome = "Angelina \" Jolie"
print(nome)
print(type(nome))


# Passar a String toda para maiúsculo (função upper())
nome = 'Geek University'
print(nome.upper())

# Passar a String toda para manúsculo (função lower())
nome = 'Geek University'
print(nome.lower())

# divide a  String (função .split()) # o padrão é utilizar o espaço como separador
nome = 'Geek University'
print(nome.split())  # Cria uma lista com a separação

# Acessando a posição 0 de uma string divida com função .split
# Também chamada de slince de string
print(nome.split(' ')[0])


# invertendo uma string slice de string
print(nome[::-1])  # aqui esta dizendo começe do primeiro elemento vai até o ultimo elemene e o inverta.

# Substituindo uma string por outra com função replace
print(nome.replace('e', 'i'))

# invertendo um texto com mesmo sentido quando invertido (Palíndromo)
texto = 'socorram me subino onibus em marrocos!'
print(texto[::-1])


