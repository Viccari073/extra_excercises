"""
Crie um programa onde o usuário possa digitar vários valores numéricos e cadraste-os em uma lista.
Caso o número já exista lá dentro, ele não séra adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
"""

valores = []

while True:
    novo = (int(input('Digite um valor: ')))
    if novo not in valores:
        valores.append(novo)
        print(f'Valor adicionado à lista!')
    else:
        print('Valor duplicado!')
    opcao = str(input('Deseja adicionar outro valor? [S/N]: '))
    if opcao in 'Nn':
        break
print()
# valores.sort() --> também pode-se colocar em ordem dessa forma
print(f'Os valores digitados foram {sorted(valores)}')
