"""
Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única
que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em oredem crescente.
"""
pares = []
impares = []
lista = [[pares], [impares]]

""" RESOLUÇÃO DO PROFESSOR: ele não usuou as variáveis 'pares' e 'impares'
lista = [[], []]
"""
for n in range(1, 8):
    numero = int(input(f'Digite o {n}º número: '))
    if numero % 2 == 0:
        pares.append(numero)
    #   lista[0].append(numero)
    else:
        impares.append(numero)
    #   lista[1].append(numero

pares.sort()
impares.sort()
# lista[0].sort()
# lista[1].sort()

print(f'A lista de números pares e imparres digitados, em ordem crescente é: \n{lista}')