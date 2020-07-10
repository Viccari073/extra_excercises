"""
Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se
encontram no intervalo de 1 até 500.
"""

s = 0  # é um acumulador (normalmente soma um valor)
cont = 0  # é um contador (normalemnte soma +1)
for n in range(1, 501, 2):
    if n % 3 == 0:
        s += n  # s = s + 1
        cont = cont + 1
print(f'A soma dos {cont} números é: {s}')
