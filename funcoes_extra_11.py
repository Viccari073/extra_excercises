"""
Faça um mini-sistema que utilize o Interactive Help do Python.
O usuário vai digitar um comando e o manual vai aparecer.
Quando o usuário digitar a palavra 'Fim', o programa se encerrará.

OBS: Use cores.
"""


def title():
    print('\033[30;43m~\033[m' * 60)
    print(f'\033[30;43m{"Interactive Help - Python":^60}\033[m')
    print('\033[30;43m~\033[m' * 60)


def function_help(msg):
    print('\033[30;44m~\033[m' * 60)
    print(f'\033[30;44m{"Acessando o manual de {msg}:":^60}\033[m')
    print('\033[30;44m~\033[m' * 60)
    help(msg)
    pass


# Programa principal
while True:
    title()
    print()
    option = str(input('Digite a função ou bilioteca que deseja consultar: '))
    var = option.upper().strip()
    if var == 'FIM':
        print('\033[30;41m~\033[m' * 60)
        print(f'\033[30;41m{"Programa finalizado!":^60}\033[m')
        print('\033[30;41m~\033[m' * 60)
        break
    else:
        function_help(option)
