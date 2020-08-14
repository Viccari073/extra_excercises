"""
Fala um programa que tenha uma função chamada escreva(), que receba um texto como parâmetro e mostre uma
mensagem com tamanho adaptável.
"""


def escreva(texto):
    tam = len(texto) + 4
    print('~' * tam)
    print(f'  {texto}')
    print('~' * tam)


# Programa principal
escreva('Lucas Viccari')
escreva('Mel')

