"""
Elabora um programa que calcule o valor a ser apgo por um produto, considerando o seu preço normal e condições
de pagamento:

- à vista com dinherio ou cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros
"""

preco = float(input('Digite o valor do produto: R$ '))
print("""Formas de pagamento:
    [1] À vista com dinheiro ou cheque
    [2] À vista no cartão
    [3] Até 2x no cartão
    [4] 3x ou mais no cartão""")
opcao = int(input('Escolha a opção: '))

if opcao == 1:
    valor_final = preco - (preco * (10/100))
    print(f'O valor a pagar, com 10% de desconto será R${valor_final: .2f}')
elif opcao == 2:
    valor_final = preco - (preco * (5 / 100))
    print(f'O valor a pagar, com 5% de desconto será R${valor_final: .2f}')
elif opcao == 3:
    parcela = preco /2
    print(f'O valor a pagar, sem desconto será R${preco: .2f}, com parcelas de R${parcela: .2f}')
elif opcao == 4:
    valor_final = preco + (preco * (20 / 100))
    total_parcela = int(input('Quantas parcelas?'))
    parcela = valor_final / total_parcela
    print(f'O valor a pagar, com 20% de juros será R${valor_final: .2f},com parcelas de R${parcela: .2f}')
else:
    print('Opção inválida, tente novamente!')

