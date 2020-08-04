"""
Crie um programa onde o usuário digite uma expressão qualqeur que use parênteses.
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos
ou fechados na ordem correta.
"""

expressao = str(input('Digite uma expressão: '))
correto = 0

for v in expressao:
    if v == '(':
        correto += 1
    elif v == ')':
        correto -= 1
if correto != 0:
    print('A expressão é inválida!')
elif correto == 0:
    print('A expressão é válida!')

''' RESPOSTA PROFESSOR
expr = str(input('Digite a expressão: '))
lista = []

for simb in expr:
    if simb == '(':
        lista.append('(')
    elif simb == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('A expressão é válida')
else:
    print('A expressao é invalida')
'''



