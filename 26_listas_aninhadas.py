"""
Listas Aninhadas

- Algumas linguagens de programação (C, Java) possuem uma estrutura de dados chamadas de Arrays:
   - Unidimensionais (Arrays/ Vetores);
   - Multidimensionais (Matrizes); 
   
Em Python  nós temos as listas

numeros = [1, 'b', 3.234, True, 5]  -> Lista ou Arrays unidimensional

 """
 
listas = [[1, 2, 3,], [4, 5, 6], [7, 8, 9]]  # Matriz 3 X 3
print(listas)
print(type(listas))

# Como fazemos para acessar os dados?
print(listas[0][1])  # 2
print(listas[2][1])  # 8


# iterando com loops em uma lista aninha
for lista in listas:
    for num in lista:
        print(num)


# List Comprehension com listas aninhadas
[[print(valor) for valor in lista] for lista in listas]

# Outros exemplos
# Gerando um tabuleiro/matrix 3x3

tabuleiro = [[numero for numero in range(1, 4)] for valor in range(1, 4)]
print(tabuleiro)