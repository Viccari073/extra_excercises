"""
Escreva um porgrama que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:

- O primeiro valor é maior;
- O segundo valor é maior;
- Os valores são iguais
"""

num1 = int(input('Digite um número inteiro: '))
num2 = int(input('Digite outro número inteiro: '))

if num1 > num2:
    print('O primeiro valor é maior.')
elif num2 > num1:
    print('O segundo valor é maior.')
else:
    print('Os valores são iguais.')
