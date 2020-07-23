"""
Crie um programa que tenha uma tupla com várias palavras (não isar acentos).
Depois mostre, para cada palavra, quais são suas vogais.
"""

palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso',
           'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado',
           'programador', 'futuro')

vogais = ('a', 'e', 'i', 'o', 'u')  # o professor não usou essa tupla
print()
print('Nas seguintes palavras, temos as seguintes vogais:')

for pos in palavras:
    print(f'\nNa palavra {pos.upper()}, temos: ', end='')
    for letra in pos:
        if letra in vogais:  # aqui ele colocou: if letra in 'aeiou':
            print(letra, end=' ')
