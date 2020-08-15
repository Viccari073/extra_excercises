"""
Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valroes inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
"""

from time import sleep


def linha():
    print('-=' * 20)


def maior(*numeros):
    linha()
    sleep(0.5)
    print('Analisando os números: ')
    cont = maior_valor = 0
    for n in numeros:
        print(f'{n}', end=' ')
        sleep(0.5)
        if cont == 0:
            maior_valor = n
        else:
            if n > maior_valor:
                maior_valor = n
        cont += 1
    print()
    print(f'Foram colocados {len(numeros)} numeros.')
#   print(f'O maior núemro é {max(numeros)}.')--> qundo usa maior() da erro, pois a função max necesita de um parametro.
    print(f'O maior número é {maior_valor}.')


# Programa principal
maior(2, 8, 9, 1, 12, 3)
maior(2, 5, 1)
maior(6)
maior()
