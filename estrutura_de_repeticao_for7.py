"""
Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
"""

n = int(input('Digite um número: '))

total = 0

for c in range(1, n+1):
    if n % c == 0:
        print('\033[33m', end='')
        total += 1
    else:
        print('\033[31m', end='')
    print(f'{c} ', end='')
print(f'\n\033[mO número {n} foi divisível {total} vezes.')
if total == 2:
    print("E por isso é um número primo")
else:
    print('E por isso ele NÃO é um número primo.')



