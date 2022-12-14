"""
Modulo Collections - Deque - (É uma lista de alta performance)

Podemos dizer que o de que é uma lista de alta perfoirmance.

"""
# Importandno deque
from collections import deque


# Criando deques

deq = deque('Geek')
print(deq)


# Adicionando elementos no deque - igual na  lista
deq.append('y')
print(deq)

# Adicionando o elemento no começo da lista(left) - Isso só tem no deque
deq.appendleft('k')
print(deq)


# Removendo elementos no final - igual na lista (remove e retorna o ultimo elemento)
deq.pop()
print(deq)

# Removendo um elemento do inicio da lista - popleft - só tem no deque
deq.popleft()
print(deq)
