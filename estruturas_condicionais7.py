"""
A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta
e mostre sua categoria de acordo com a idade:

- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JUNIOR
- Até 20 anos: SÊNIOR
- Acima: MASTER
"""
from datetime import date

ano = date.today().year

nasc = int(input('Digite o ano de nascimento: '))
idade = ano - nasc

if idade <= 9:
    print(f'Com {idade} anos, você está na categoria MIRIM.')
elif 9 < idade <= 14:
    print(f'Com {idade} anos, você está na categoria INFANTIL.')
elif 14 < idade <= 19:
    print(f'Com {idade} anos, você está na categoria JUNIOR.')
elif 19 < idade <= 25:
    print(f'Com {idade} anos, você está na categoria SÊNIOR.')
elif idade > 25:
    print(f'Com {idade} você está na categoria MASTER.')

    
