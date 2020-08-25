"""
Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um
dicionário com as seguintes informações:

- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)

Adicione também as docstrings da função
"""


def notas(*n, sit=False):
    """
    -> Function that analyzes a student's grades and situation (optional).
    :param n: undetermined amount of grades.
    :param sit: if requested, it returns the student's situation.
    :return: dict ficha
    """
    ficha = {'total': len(n),
             'maior': max(n),
             'menor': min(n),
             'media': sum(n)/len(n)}
    if sit:
        if sum(n)/len(n) >= 7:
            ficha['situação'] = 'Boa'
        elif 5 <= sum(n)/len(n) <= 6.9:
            ficha['situação'] = 'Razoável'
        else:
            ficha['situação'] = 'Ruim'
    return ficha


resp = notas(3.5, 10,  8.5, 9, 1.5, 8, sit=True)
print(resp)
help(notas)
