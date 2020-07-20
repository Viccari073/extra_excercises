"""
Crie um programa que vai gerar cinco vnúeros aleatórios e colocar em uma tupla.

Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
"""

from random import randint

numeros = (randint(1, 20), randint(1, 20), randint(1, 20), randint(1, 20), randint(1, 20))

print('Os números sorteados foram: ', end='')

for n in numeros:
    print(f' {n} ', end='')

print()
print(f'O maior número sorteado foi: {max(numeros)}')
print(f'O menor número sorteado foi: {min(numeros)}')
