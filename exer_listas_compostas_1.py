"""
Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:

A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
"""

cadastro = list()
dados = list()
mais_pesado = menos_pesado = 0

while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(cadastro) == 0:
        mais_pesado = menos_pesado = dados[1]
    else:
        if dados[1] > mais_pesado:
            mais_pesado = dados[1]
        if dados[1] < menos_pesado:
            menos_pesado = dados[1]
    cadastro.append(dados[:])
    dados.clear()
    opcao = str(input('Deseja cadastrar mais nomes? [S/N]: '))
    if opcao in 'Nn':
        break

print()
print(f'Os dados cadastrados foram: {cadastro}')
print()
print(f'Foram cadastradas {len(cadastro)} pessoas.')
print(f'O maior peso foi de {mais_pesado}Kg. Peso de: ', end='')
for p in cadastro:
    if p[1] == mais_pesado:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi de {menos_pesado}Kg. Peso de: ', end='')
for p in cadastro:
    if p[1] == menos_pesado:
        print(f'[{p[0]} ]')
