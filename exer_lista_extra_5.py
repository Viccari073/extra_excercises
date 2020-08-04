"""
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão contar apenas os valores pares e os valores ímpares digitados.
Ao final, mostre o conteúdo das três listas.
"""

lista_principal = []
lista_pares = []
lista_impares = []

while True:
    num = int(input('Digite um valor: '))
    lista_principal.append(num)
    opcao = str(input('Deseja continuar? [S/N]: '))
    if num % 2 == 0:
        lista_pares.append(num)
    elif num % 2 != 0:
        lista_impares.append(num)
    if opcao in 'Nn':
        break

"""
SOLUÇÃO DO PROFESSOR:

Após o loop do while:

for i, v in enumerate(lista_principal)
    if v % 2 == 0:
        lista_pares.append(v)
    elif v % 2 == 1:
    lista_impares.append(v)
"""
print()
print(f'A lista principal é: {lista_principal}')
print(f'A lista de números pares é: {lista_pares}')
print(f'A lista de números ímpares é {lista_impares}')
