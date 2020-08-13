"""
Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou.
Depois vai ler a quantidade de gols feitos em cada partida.
No final, tudo isso será mostrado em um dicionário, incluindo o total de gols feitos durante o campeonato.
"""

aprov = {}

aprov['Nome do jogador'] = str(input('Nome do Jogador: '))
quant_partidas = int(input(f'Quantas partidas {aprov["Nome do jogador"]} jogou: '))

gols = []

for g in range(0, quant_partidas):
    gols.append(int(input(f'Quantos gols na {g + 1}ª partida? ')))
    aprov['Gols'] = gols[:]
aprov['Total de gols'] = sum(gols)
print('-=' * 20)
print(aprov)
print('-=' * 20)
for i, v in aprov.items():
    print(f'{i}: {v}')
print('-=' * 20)
print()
print(f'O jogador {aprov["Nome do jogador"]} jogou {quant_partidas} partidas.')
for i, v in enumerate(aprov['Gols']):
    print(f'  => Na {i + 1}ª partida, marcou: {v} ')
print()
print(f'Foi um total de {sum(gols)} gols.')
