"""
Faça um programa que ajude um jogador da mega sena a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
cadastrando tudo em uma lista composta.
"""

from random import randint
from time import sleep

lista_jogos = []
jogos = []

print()
quant = int(input('Quantos jogos deseja fazer? '))
total = 1

while total <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in jogos:
            jogos.append(num)
            cont += 1
        if cont >= 6:
            break
    jogos.sort()
    lista_jogos.append(jogos[:])
    jogos.clear()
    total += 1
print()
print('=' * 6, f'SORTEANDO {quant} JOGOS', '=' * 6)
for i, v in enumerate(lista_jogos):
    print(f'Jogo {i +1}: {v}')
    sleep(1)
print()
print('=' * 10, 'BOA SORTE', '=' * 11)
