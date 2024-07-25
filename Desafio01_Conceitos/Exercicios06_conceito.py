'''
Escreva um programa que calcule o tempo de uma viagem. Faça um
comparativo do mesmo percurso de avião, carro e ônibus.
Levando em consideração:
● avião = 600 km/h
● carro = 100 km/h
● ônibus = 80 km/h
'''

def calcular_tempo_viagem(duracao, velocidade):
    return duracao / velocidade

aviao = 600
carro = 100
onibus = 80

duracao = int(input('Quantos Km tem a sua viagem? '))

tempo_aviao = calcular_tempo_viagem(duracao, aviao)
tempo_carro = calcular_tempo_viagem(duracao, carro)
tempo_onibus = calcular_tempo_viagem(duracao, onibus)

print(f"Tempo de viagem para {duracao} km:")
print(f"Avião: {tempo_aviao:.2f} horas")
print(f"Carro: {tempo_carro:.2f} horas")
print(f"Ônibus: {tempo_onibus:.2f} horas")
