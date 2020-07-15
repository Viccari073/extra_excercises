"""
Crie um programa que leia uma frase qualquer e diga se ela pe um palíndromo,
descosiderando os espaços.
"""

frase = str(input('Deigite uma frase: ')).strip().upper()  # strip - tirar os espaços. Upper para deixar tudo maiúsculo.
palavras = frase.split()  # split para separar a frase em palavras (forma uma lista).
junto = ''.join(palavras) # juntou tudo em uma strig só.
inverso = ''

# Forma muito mais simples, mas sem a utilização do for:
# inverso = junto[::-1]

for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(junto, inverso)
if inverso == junto:
    print('Temos um palpindromo.')
else:
    print('Não temos um palíndromo.')
