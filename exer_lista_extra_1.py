"""
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
"""

valores = []

for v in range(0, 5):
    valores.append(int(input(f'Digite o valor da posição {v}: ')))

maior = max(valores)
menor = min(valores)

print(f'Os valores digitados foram: {valores}')
print()
print(f'O maior valor da lista é o: {maior}, na posição ', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}...', end='')
print()
print(f'O mneor valor da lista é o: {menor}, na posição ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}...', end='')
print()

''' RESOLUÇÃO DO PROFESSOR
valores = []
maior = 0
menor = 0

for v in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {v}: ')))
    if v == 0:
        maior = menor = valores[v]
    else:
        if valores[v] > maior:
            maior = valores[v]
        if valores[v] < menor:
            menor = valores[v]
print()
print(f'Os valores digitados são: {valores}')
print(f'O maior valor digitado foi: {maior} na(s) posição(s): ', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}...', end='')
print()
print(f'O menor valor digitado foi: {menor} na(s) posição(s): ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}...', end='')
'''
