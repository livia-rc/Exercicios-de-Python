#Enunciado: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
#A) qual é o total gasto na compra.
#B) quantos produtos custam mais de R$1000.
#C) qual é o nome do produto mais barato.

print('----- CADASTRO DE PRODUTOS -----')

total_compra = quant_produto = menor_preco = 0
produto_menor_valor = ''

while True:
    nome = str(input('\nDigite o nome do produto: '))
    preco = float(input('Digite o preço do produto: R$'))

    total_compra += preco

    if preco > 1000:
        quant_produto += 1

    if menor_preco == 0 or preco < menor_preco:
        menor_preco = preco
        produto_menor_valor = nome

    op = str(input('\nVocê deseja cadastrar mais um produto (SIM ou NÃO)? ')).upper()

    if op == 'NÃO':
        print('\nTotal da compra: R${:.2f}\n{} produtos custam mais de R$1000,00\n{} é o produto mais barato'.format(total_compra,quant_produto, produto_menor_valor))
        print('Programa encerrado!')
        break