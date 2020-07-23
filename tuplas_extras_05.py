'''
Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.

No final, mostre uma listagem de preços, organizando os dados em forma tabular.
'''

lista_produtos = ('Pão frânces', 1.99,
                  'Mussarela', 7.99,
                  'Presunto', 5.60,
                  'Salaminho', 14.99,
                  'Pão de queijo', 6.00,
                  'Pão na chapa', 2.50,
                  'Misto quente', 7.50)
print('=' * 40)
print(f'{"LISTA DE PREÇOS":^40}')
print('=' * 40)
for posicao in range(0, len(lista_produtos)):
    if posicao % 2 == 0:
        print(f'{lista_produtos[posicao]:.<32}', end='')
    else:
        print(f'R$ {lista_produtos[posicao]:>5.2f}')


