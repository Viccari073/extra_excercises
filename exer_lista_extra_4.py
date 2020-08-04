"""
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
"""

valores = []

while True:
    num = int(input('Digite um valor: '))
    valores.append(num)
    opcao = input('Deseja continuar? [S/N]: ')
    if opcao in 'Nn':
       break
valores.sort(reverse=True)
print()
print(f'Foram digitados {len(valores)} números.')
print(f'A lista de forma decrescente é: {valores}')
if 5 in valores:
    print('O número 5 foi digitado e está na lista.')
else:
    print('O número 5 não foi digitado, portanto, não está na lista.')

