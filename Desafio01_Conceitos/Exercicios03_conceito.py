'''
Faça um Programa que peça a quantidade de quilômetros, transforme
em metros, centímetros e milímetros.

'''
quilometro = float(input('Digite a quantidade em metros: '))

metros = quilometro * 1000
centimetros = quilometro * 100000
milimetros = quilometro * 1000000

print(f'{quilometro} quilometros é igual a {metros} metros')
print(f'{quilometro} quilometros é igual a {centimetros} centímetros')
print(f'{quilometro} quilometros é igual a {milimetros} milímetros')

