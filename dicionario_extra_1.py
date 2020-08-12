"""
Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
No final, mostre o conteúdo da estrutura na tela.
"""

cadastro = dict()

cadastro['nome'] = str(input('Nome: '))
media = float(input(f'Media de {cadastro["nome"]}: '))
cadastro['media'] = media
if media >= 7.0:
    cadastro['situacao'] = 'APROVADO'
elif media < 7.0:
    cadastro['situacao'] = 'REPROVADO'

print(f'Com a média de {cadastro["media"]}, o aluno {cadastro["nome"]} está {cadastro["situacao"]}!')

""" EXEMPLO PROFESSOR
for k, v in aluno.items():
    print(f'{k} é igual a {v}')
"""
