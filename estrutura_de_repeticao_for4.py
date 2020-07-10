"""
Faça um programa que mostre um número que o usuário escolher, utilizando um laço for.
"""

n = int(input('Digite um número para ver sua tabuada: '))

for c in range(1, 11):
    # print(c * n) - resolução somente com os resultados.
    print(f'{n} x {c} = {n*c}')