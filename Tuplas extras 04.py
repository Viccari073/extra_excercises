"""
Desenvolva um programa que leia quator valores pelo teclado e guarde-os em uma tupla. No final mostre:

A) Quantas vezes apareceu o número 9.
B) Em qual posição foi digitado o promeiro número 3.
C) Quais foram os números pares.
"""

# Resolução do professor:
# numeros = (int(input('\nDigite o primerio número: '),
#            int(input('Digite o segundo número: '))
#            int(input('Digite o terceiro número: '))
#            nt(input('Digite o quarto número: ')))

print('Digite 4 números de 0 a 10!')
num = int(input('\nDigite o primerio número: '))
num1 = int(input('Digite o segundo número: '))
num2 = int(input('Digite o terceiro número: '))
num3 = int(input('Digite o quarto número: '))

numeros = (num, num1, num2, num3)
print(f'Você escolheu os números: {numeros}')
print(f'O número 9 apareceu {numeros.count(9)} vez(s).')

if 3 in numeros:
    print(f'O número 3 apareceu na {numeros.index(3)+1}ª posição.')
else:
    print('O valor 3 não aparece em nenhuma posição.')
print(f'Os valores pares digitados foram: ', end='')
for n in numeros:
    if n % 2 == 0:
        print(n, end=' ')

