"""
Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
No final, mostre a matriz na tela, com a formatação correta e mostre:

A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.
"""

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_pares = soma_terceira_coluna = maior_segunda_linha = 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = (int(input(f'Digite um valor para o espaço [{l}, {c}]:  ')))
        if matriz[l][c] % 2 == 0:
            soma_pares += matriz[l][c]
        if matriz[l][2]:
            soma_terceira_coluna += matriz[l][2]
        if matriz[1][c] > maior_segunda_linha:
            maior_segunda_linha = matriz[1][c]

print()
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()

print()
print(f'A soma dos valores pares é: {soma_pares}')
print(f'A soma dos valores da terceira coluna é: {soma_terceira_coluna}')
print(f'O maior valor da segunda linha é: {maior_segunda_linha}')

