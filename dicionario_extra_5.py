"""
Crie um programa que leia nome, sexo e idade de várias pessoas, guardadno os dados de cada pessoa em um dicionário e
todos os dicionários em uma lista.
No final, mostre:

A) Quantas pessoas foram cadastradas.
B) A média de idade do grupo.
C) Uma lista com todas as mulheres.
D) Uma lista com todas as pessoas, com idade acima da média.
"""

cadastro = list()
media_idade = list()
mulheres = list()
idade_acima_media = list()

while True:
    pessoas = dict()
    pessoas['Nome'] = str(input('Nome: '))
    pessoas['Sexo'] = str(input('Sexo [M/F]: ')).upper()[0]  # transforma em maiúsculas e pega somente a primeira letra
    if pessoas['Sexo'] not in 'MF':
        print('Digite apenas M ou F.')
        pessoas['Sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
    if pessoas['Sexo'] in 'F':
        mulheres.append(pessoas['Nome'])
    pessoas['Idade'] = int(input('Idade: '))
    media_idade.append(pessoas['Idade'])
    cadastro.append(pessoas.copy())
    pessoas.clear()
    opcao = str(input('Deseja cadastrar mais pesoas? [S/N]: ')).upper()[0]
    if opcao not in 'SN':
        print('Opção incorreta! Escoha entre S ou N.')
        opcao = str(input('Deseja cadastrar mais pesoas? [S/N]: ')).upper()[0]
    if opcao in 'N':
        break
print('-=' * 20)
print(cadastro)
print()
print(f'A) Foram cadastradas {len(cadastro)} pessoas.')
print(f'B) A media de idade do grupo é {sum(media_idade) / len(cadastro): .2f}.')
print(f'C) A lista de mulheres cadastradas é: {mulheres}')
print('D) A lista de pessoas com idade acima da média é: ')
for p in cadastro:
    if p['Idade'] >= sum(media_idade) / len(cadastro):
        for k, v in p.items():
            print(f'   --> {k} = {v}; ', end='')
        print()


