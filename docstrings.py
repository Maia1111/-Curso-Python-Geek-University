"""
Documentando funções com Docstrings

# Retorna Docstring da função print
print(help(print))


"""

def diz_oi():
    """uma função simples que retorna string oi 
    """
    return 'oi'


#print(help(diz_oi))

print(diz_oi.__doc__) # Metodo  .__doc__ que retorna a docstring de uma função
print(print.__doc__)


def exponencial(num1, potencia=2):
    """
    Argumentos:
      Função recebe o argumento num1 e faz a potenciação pelo segundo arumento opcional,
      caso não declare nada  a potenciação será por 2
        num1 (_type_): Parâmetro obrigatório
        potencia (int, optional): Parâmetro opcional, default 2
    """
    return num1 ** potencia
    
    
print(help(exponencial))
