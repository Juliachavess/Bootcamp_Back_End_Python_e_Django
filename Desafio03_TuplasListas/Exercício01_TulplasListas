'''Utilizando listas faça um programa que faça 5 perguntas para uma
pessoa sobre um crime.
As perguntas são:
""Telefonou para a vítima?""
""Esteve no local do crime?""
""Mora perto da vítima?""
""Devia para a vítima?""
""Já trabalhou com a vítima?""
O programa deve no final emitir uma classificação sobre a participação
da pessoa no crime.
Se a pessoa responder positivamente a 2 questões ela deve ser
classificada como ""Suspeita"", entre 3 e 4 como ""Cúmplice"" e 5 como
""Assassino"".
Caso contrário,ele será classificado como""Inocente"".
'''
lista = []

print('Responda as perguntas digitando 1 para sim e 2 para não!')
telefone = int(input('Telefonou para a vítima? '))
if telefone == 1:
    lista.append(telefone)
local = int(input('Esteve no local do crime? '))
if local == 1:
    lista.append(local)
mora = int(input('Mora perto da vítima? '))
if mora == 1:
    lista.append(mora)
devia = int(input('Devia para a vítima? '))
if devia == 1:
    lista.append(devia)
trabalha = int(input('Já trabalhou com a vítima? '))
if trabalha == 1:
    lista.append(mora)

tamanho_lista = len(lista)

if tamanho_lista == 5:
    classificacao = "Assassino"
elif 3 <= tamanho_lista <= 4:
    classificacao = "Cúmplice"
elif tamanho_lista == 2:
    classificacao = "Suspeita"
else:
    classificacao = "Inocente"

print(f"A classificação final é: {classificacao}")

