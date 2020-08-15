"""
Crie um programa que tenha um função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
retornando um valor literal indicando se uma pessoa tem voto negado, opcional ou obrigatório nas eleições.
"""


def voto(ano):
    from datetime import datetime  # colocar dentro da função economiza memória.
    atual = datetime.now().year
    dif = atual - ano
    if dif < 16:
        return print(f'Com {dif} o voto é NEGADO!')
    elif 16 <= dif < 18 or dif > 65:
        return print(f'Com {dif} o voto é OPCIONAL!')
    else:
        return print(f'Com {dif} o voto é OBRIGATÓRIO!')


print()
voto(int(input('Digite a data de nascimento: ')))
