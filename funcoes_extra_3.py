"""
Faça uma função chamada contador(), que receba três parâmetros: inicio, fim e passo e realize a contagem.

Seu programa tem que realizar três contagens através da função criada:

1) De 1 até 10, de 1 em 1
2) De 10 até 0, de 2 em 2
3) Uma contagem personalizada.
"""

from time import sleep


def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('-=' * 25)
    print(f'A contagem de {i} até {f} de {p} em {p} é: ')
    sleep(2)
    if i < f:
        cont = 1
        while cont <= f:
            print(f'{cont}', end=' ')
            sleep(0.5)
            cont += 1
        print()
    else:
        cont = i
        while cont >= f:
            print(f'{cont}', end=' ')
            cont -= p
            sleep(0.5)
        print()


# Prpgrama principal
contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 25)
print('Escolha agora o início, o fim e o passador:')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)

