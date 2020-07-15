"""
Crie um programa que leia o ano de anscimento de sete pessoas.
No final, mostre quantas pessoas ainda não atongiram a maioridade e quantas já são maiores.
"""

from datetime import date

ano_atual = date.today().year
pessoas_maiores = 0
pessoas_menores = 0

for a in range(1, 8):
    nasc =int(input(f'Digite o ano de nascimento da {a}ª pessoa: '))
    if ano_atual - nasc < 18:
        pessoas_menores += 1
    elif ano_atual - nasc >= 18:
        pessoas_maiores += 1

print()
print(f'{pessoas_menores} são menores de idade.')
print(f'{pessoas_maiores} são maiores de idade.')


