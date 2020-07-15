"""
Desenvolva um porgrama que leia o primeiro termo e a razão de uma Progressão Aritimética.
No final, mostre os 10 primeiros termos dessa progressão.
"""
n = int(input('Digite o primeiro termo: '))
p = int(input('Digite a razão: '))
decimo = n + (10 - 1) * p  # fórmula da PA para achar o decimo número. Se fosse 15, é só substituir o 10 pelo 15, etc.)

for c in range(n, decimo + p, p):
    print(f'{c}', end = ' -> ')
print('PRONTO')