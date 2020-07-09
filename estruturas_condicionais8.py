"""
Defina se 3 valores podem formar um triângulo e mostre que tipo de triângulo será formado:

- EQUILÁTERO: todos os lados são iguais
- ISÓSCELES: dois lados são iguais
- ESCALENO: todos os lados são diferentes
"""

lado1 = float(input('Digite o primeiro valor: '))
lado2 = float(input('Digite o segundo valor: '))
lado3 = float(input('Digite o terceiro valor: '))

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado2 + lado1:
    if lado1 == lado2 == lado3:
        print('Esses valores correspondem a um triângulo EQUILÁTERO.')
    elif lado1 == lado2 or lado2 == lado3 or lado3 == lado1:
        print('Esses valores correspondem a um triângulo ISÓSCELES.')
    else:
        print('Com todos os lados diferentes, os valores correspondem a um triângulo ESCALENO.')
else:
    print('Esses valores não correspondem a um triângulo.')