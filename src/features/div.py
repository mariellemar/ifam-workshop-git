# src/features/add.py

def div(a, b):
    """
    Função para somar dois números.
    
    :param a: Primeiro número
    :param b: Segundo número
    :return: A soma de a e b
    """
    if (b!=0):
        res = a/b
    else:
        res = "Impossível dividir por 0"

    return res
