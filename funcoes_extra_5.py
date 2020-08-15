"""
Faça um programa que tenha uma lista chamada números e duas funções chamdas sorteio() e soma_par().
A primeira vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma
entre todos os valores pares sorteados pela funçao anterior.
"""

from random import randint
from time import sleep


def sorteio(lista):  # nome lista é aleatório
    print(f'Sorteando 5 valores da lista: ', end='')
    for n in range(0, 5):
        num = randint(1, 10)
        lista.append(num)
        print(f'{num} ', end='')
        sleep(0.5)
    print()


def soma_par(lista):
    soma = 0
    for n in lista:
        if n % 2 == 0:
            soma += n
    print(f'A soma dos números pares de {lista} é: {soma}')


# Programa principal
numeros = list()
sorteio(numeros)
soma_par(numeros)
