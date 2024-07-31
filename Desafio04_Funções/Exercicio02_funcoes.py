# Reverso do número. Faça uma função que retorne o reverso de um
# número inteiro informado. Por exemplo: 127 -> 721

def reverso(numero):
    numero_reverso = str(numero)[::-1]
    return int(numero_reverso)

resultado = reverso(1985)
print(resultado)  
