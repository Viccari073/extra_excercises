"""
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol (2019), na ordem
de colocação. Depois mostre:

A) Apenas os 5 primeiros colocados.
B) Os últimos 4 colocados.
C) Uma lista com os times em ordem alfabética.
D) Em qual posição na tabela está o tima do São Paulo.
"""

tabela = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Atlhetico-PR',
          'São Paulo', 'Internacional', 'Corinthians', 'Fortaleza', 'Goiás',
          'Bahia', 'Vasco', 'Atlético-MG', 'Fluminense', 'Botafogo',
          'Ceará', 'Cruzeiro', 'CSA', 'Chapecoense', 'Avaí')
print()
print(tabela)  # Foi o que eu fiz
# for times in tabela:  # Possibilidade que o professor deu.
#    print(times)

print('=-' * 90)
print()
print(f'Os primeiros 5 colocados são: {tabela[0:5]}')
print(f'Os últimos 4 colocados são: {tabela[-4:]}')
print()
print(f'Os times do campeonato, em ordem alfabética são:\n{sorted(tabela)}')
print()
posição_SP = tabela.index('São Paulo') + 1
print(f'O São Paulo está na {posição_SP}ª colocação')
