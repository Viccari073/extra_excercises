"""
Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e
quantos gols ele marcou.

O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
"""


def ficha(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} gol(s).')


# Programa principal
n = str(input('Nome do jogador: '))
g = str(input('Números de gols: '))  # ler como string, pois se não colocar nada não da erro.
if g.isnumeric():  # verifica de a variável recebeu um número
    g = int(g)  # transforma a string em inteiro
else:
    g = 0
if n.strip() == '':  # verificca se a variável n ficou vazia ou não.
    ficha(gols=g)
else:
    ficha(n, g)
