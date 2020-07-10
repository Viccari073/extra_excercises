"""
Desenvolva um programa que leia seis números interios e mostre a soma apenas daqueles que forem pares.
Se o valor digitado for ímpar, desconsidere-os.
"""

s = 0
cont = 0
for n in range(1, 7):
    num = int(input(f'Digite o {n}º número: '))
    if num % 2 == 0:
        s += num
        cont += 1
print()
print(f'Você informou {cont} números PARES e a soma deles é {s}')
