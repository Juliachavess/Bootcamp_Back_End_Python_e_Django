'''Peça ao usuário para informar o ano de nascimento. Em seguida,
calcule e imprima a idade atual.'''

from datetime import datetime

ano_atual = datetime.now().year

nascimento = int(input('Digite o ano do seu nascimento: '))

idade = ano_atual - nascimento
print(f'Sua idade é: {idade}')


