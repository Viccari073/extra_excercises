"""
Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário.
Se por acaso a CTPS for diferente de zero, o dicionário receberá também o ano de contratação e o salário.
Calcule e acrescente, além da idade, com quantos anos a pessoa vai e aposentar.
"""

from datetime import datetime

cadastro = dict()

cadastro['Nome'] = str(input('Nome: '))
nasc = int(input('Ano de nasciemnto: '))
idade = datetime.now().year - nasc
# cadastro['Idade'] = datetime.now().year - nasc
cadastro['Idade'] = idade
cadastro['Ctps'] = int(input('Carteira de trabalho (0 não tem):'))
if cadastro['Ctps'] != 0:
    cadastro['Contratacao'] = int(input('Ano de contratação: '))
    cadastro['Salario'] = float(input('Salário: R$ '))
    cadastro['Aposentadoria'] = cadastro['Idade'] + ((cadastro['Contratacao'] + 35) - datetime.now().year)

print('=' * 30)
print()

print(cadastro)
for i, v in cadastro.items():
    print(f'{i} é: {v}')



