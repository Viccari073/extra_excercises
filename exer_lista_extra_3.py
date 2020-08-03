"""
Crie um programa onde o usuário possa digitar conco valçores numéricos e cadastre-os em uma lista,
já na posição correta de inserção (sem usar o sort()).
No final, mostre a lista ordenada na tela.
"""

valores = []
posicao = 0

for v in range(0, 5):
    num = int(input('Digite um valor: '))
    if v == 0 or v > valores[-1]:
        valores.append(num)
    else:
        while posicao < len(valores):
            if v <= valores[posicao]:
                valores.insert(posicao, num)
                break
            posicao += 1
print('A lista ordenada é: ')
print(valores)
