"""
Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:

- 1 para binário
- 2 para octal
- 3 para hexadecimal
"""

numero = int(input('Digite um número inteiro: '))
print('Escolha a base de conversão:'
      '\n[1] para binário'
      '\n[2] para octal'
      '\n[3] para hexadecimal')
opcao = int(input('Digite sua opção: '))

if opcao == 1:
    print(f'O número {numero} em binário é igual a {bin(numero)[2:]}')  # [2:] tira o Ob (símbolo para binário)
elif opcao == 2:
    print(f'O número {numero} em octal é igual a {oct(numero)[2:]}')  # [2:] tira o Oo (símbolo para octal)
elif opcao == 3:
    print(f'O número {numero} em hexadecimal é igual a {hex(numero)}')  # [2:] tira o Ox (símbolo para hexadecimal)
else:
    print('Opção inválida!')