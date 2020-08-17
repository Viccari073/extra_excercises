"""
Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante à função input() do Python,
só que fazendo a validação para aceitar apenas um valor numérico.

Ex:
n = leiaInt('Digite um número: ')
"""


def leia_int(numero):
    while True:
        valor = str(input(numero))
        if valor.isnumeric():
            valor = int(valor)
            return valor
            break
        else:
            print('\033[31mErro! Digite um número válido.\033[m')


# Programa principal
n = leia_int('Digite um número: ')  # ATENÇÃO -> NÃO PRECISA DO INPUT
print(f'Você digitou o número {n}')

