"""
Tipo Boleadno

Algebra Booleana, criada por George Boole

Geralmente agente tem duas constante (Verdadeiro ou Falso)

True -> Verdadeiro
False -> Falso

Sempre  com as iniciais maiúsculas
"""

ativo = True

"""
Operações Básicas

"""

# Negação (not)

"""
Fazendo a negação, se o valor booleano for verdadeiro o resultado será falso,
se o resultado for falso o resultado será verdadeiro. Ou seja, sempre o contário.

"""
print(not ativo)

# Operador E (and)
"""
Também é uma operação binária, ou seja, depende de dois valores.
onde pelo menos um dos valores tem que ser verdadeiro.


True and True -> True
True and False -> True 
False and True -> True 
False and False -> False
"""

# Operador Ou (or)
"""
Também é uma operação binária tambem depende de dois valores. 
Ambos devem ser verdadeiros para  que o retorno seja verdadeiro.

True or True -> True 
True or False -> False
False or True -> False 
False or False -> False

"""