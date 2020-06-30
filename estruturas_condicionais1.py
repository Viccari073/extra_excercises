"""
Escreva um porgrama para aprovar um empréstimo bancário para a compra de uma casa.
O programa vai perguntar o valor da casa, o salário do comprodor e em quanos anos ele vai pagar.

Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário, ou então o empréstimo será negado.
"""

valor_casa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual seu salário? R$'))
anos = int(input('Em quantos anos pretende quitar o empréstimo? '))

meses = anos * 12

prestacao = valor_casa / meses

if prestacao >= salario * (30/100):
    print(f'A prestação de R${prestacao: .2f} excede 30% do seu salário.')
    print('Empréstimo negado')
else:
    print(f'A prestação será de R${prestacao: .2f}')
    print('Empréstimo aprovado!')

