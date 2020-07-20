"""
Crie um programa que tenha uma tupla totalemnte preenchida com uma contagem por extenso, de zero até vinte.

Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
"""

cont = ('zero', 'um', 'doi', 'três', 'quantro', 'cinco',
        'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
        'doze', 'treze', 'quatorze', 'quinze', 'dezesseis',
        'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:  # Validação para ver se o número está dentro do limite.
    num = int(input('Digite um número de 0 a 20: '))
    if 0 <= num <= 20:
        break
    print('Tente novamente.', end=' ')
print(f'Você digitou o número {cont[num]}')