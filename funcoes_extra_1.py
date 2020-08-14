"""
Faça um porgrama que tenha uma função chamada área(), que receba as dimensões de um terreno retangular
(largura e comprimento) e mostra a área do terreno.
"""


def area(larg, comp):
    a = larg * comp
    print(f'A área de um terreno de {larg} x {comp} é {a} m²')  # ALT direito + 2 (m²)


# Programa principal
print('   Controle de terrenos')
print('-' * 28)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)

""" Poderai ser assim:
area(l=float(input('Largura:')),c=float(input('Comprimento:')))
"""
