'''
Escreva um programa que calcule o salário líquido. Lembrando de
declarar o salário bruto e o percentual de desconto do Imposto de
Renda.
● Renda até R$ 1.903,98: isento de imposto de renda;
● Renda entre R$ 1.903,99 e R$ 2.826,65: alíquota de 7,5%;
● Renda entre R$ 2.826,66 e R$ 3.751,05: alíquota de 15%;
● Renda entre R$ 3.751,06 e R$ 4.664,68: alíquota de 22,5%;
● Renda acima de R$ 4.664,68: alíquota máxima de 27,5%.
'''

salario_bruto = float(input('Informa o seu salário Bruto R$  '))

if salario_bruto <= 1903.98:
    aliquota = 0
elif salario_bruto <= 2826.65:
    aliquota = 0.075
elif salario_bruto <= 3751.05:
    aliquota = 0.15
elif salario_bruto <= 4664.68:
    aliquota = 0.225
else:
    aliquota = 0.275

desconto_ir = salario_bruto * aliquota
liquido = salario_bruto - desconto_ir

print(f'Com um salário bruto de R$ {salario_bruto}, o desconto do Imposto de '
      f'Renda será de {aliquota * 100:.2f}% e seu salário líquido será de R$ {liquido}')