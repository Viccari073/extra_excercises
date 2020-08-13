"""
Crie um programa que gerencie o aproveitamento de VÁRIOS jogadorES de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou.
Depois vai ler a quantidade de gols feitos em cada partida.
No final, tudo isso será mostrado em um dicionário, incluindo o total de gols feitos durante o campeonato,
além de um sitema de visualização de detalhes do aproveitaneto de cada jogador
"""

time = list()
aprov = dict()
gols = list()

while True:  # Ler os dados de cada jogador
    aprov.clear()
    aprov['Nome do jogador'] = str(input('Nome do Jogador: '))
    quant_partidas = int(input(f'Quantas partidas {aprov["Nome do jogador"]} jogou: '))
    gols.clear()
    for g in range(0, quant_partidas):
        gols.append(int(input(f'Quantos gols na {g + 1}ª partida? ')))
        aprov[' Gols'] = gols[:]
    aprov['  Total de gols'] = sum(gols)
    time.append(aprov.copy())
    while True:
        print()
        opcao = str(input('Deseja cadastrar  outro jogador? [S/N]: ')).upper()[0]
        if opcao in 'SN':
            break
        print('ERRO! Digite apenas S ou N.')
    if opcao == 'N':
        break

# Começar a análise de dados
print('-=' * 30)
print('Cod ', end='')
for i in aprov.keys():
    print(f'{i:<18} ', end='')
print()
print('-' * 60)
for k, v in enumerate(time):
    print(f'{k:>1} ', end='')
    for d in v.values():
        print(f'  {str(d):<18}', end='')
    print()

print('-' * 60)
while True:
    busca = int(input('Mostrar dados de qual jogador? [999 finaliza]: '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com o código {busca}')
    else:
        print(f'Levantamento do jogador {time[busca]["Nome do jogador"]}:')
        for i, g in enumerate(time[busca][' Gols']):
            print(f'     - No jogo {i + 1} fez {g} gols.')
    print('-' * 60)
print()
print('               << FINALIZANDO >>')

















