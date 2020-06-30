"""
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:

- Se ele ainda vai se alistar ao serviço militar;
- Se é a hora de se alistar;
- Se já passou do tempo do alistamento.

Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
"""

from datetime import date  # pega o ano atual

ano_nasc = int(input('Digite o ano do seu nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano_nasc

print(f'Quem nasceu em  {ano_nasc} tem {idade} anos.')

if idade == 18:
    print(f'Com {idade} você deve se alistar imediatamente!')
elif idade < 18:
    saldo = 18 - idade
    print(f'Ainda faltam {saldo} ano(s) para o alistamento.')
    ano = ano_atual + saldo
    print(f'Seu alistamento será {ano}.')
else:  # elif idade > 18:
    saldo = idade - 18
    print(f'Você deveria ter se alistado à {saldo} ano(s).')
    ano = ano_atual - saldo
    print(f'Seu alistamento foi {ano}.')

