"""
Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
No final, mostre um boletrom contendo a média de cada um e permite que o usuário possa mostrar as notas de
cada um individualemnte.
"""


boletin = []

while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 01: '))
    nota2 = float(input('Nota 02 : '))
    media = (nota1 + nota2) / 2
    boletin.append([nome, [nota1, nota2], media])
    opcao = str(input('Deseja cadastrar mais? [S/N]'))
    if opcao in 'Nn':
        break

print()
print(f'{"No.":<4}{"NOME":<8}{"MEDIA":>6}')
print('-' * 30)
for i, v in enumerate(boletin):
    print(f'{i:<4}{v[0]:<10}{v[2]:<10.1f}')

print('-' * 30)
print()
while True:
    opcao2 = int(input('Deseja mostrar a nota de qual aluno? (999 interrompe): '))
    if opcao2 <= len(boletin) - 1:
        print(f'As notas de {boletin[opcao2][0]} são: {boletin[opcao2][1]}')
        print()
    if opcao2 == 999:
        break
