#Enunciado:  Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#– à vista dinheiro/cheque: 10% de desconto
#– à vista no cartão: 5% de desconto
#– em até 2x no cartão: preço formal 
#– 3x ou mais no cartão: 20% de juros

valor_normal = float(input('Digite o preço de um produto em R$: '))

op = int(input('Formas de pagamentos\n1. À vista dinheiro/cheque (10% de desconto)\n2. À vista no cartão (5% de desconto)\n3. Em até 2x no cartão (Sem desconto)\n4. 3x ou mais no cartão (20% de juros)\nEscolha uma opção: '))


if op == 1 :
    valor_com_desconto = valor_normal * 0.9
    print('Essa forma de pagamento pussui um desconto de 10%, portanto o preço do produto com desconto será de R${:.2f}'.format(valor_com_desconto))
elif op == 2 :
    valor_com_desconto = valor_normal * 0.95
    print('Essa forma de pagamento pussui um desconto de 5%, portanto o preço do produto com desconto será de R${:.2f}'.format(valor_com_desconto))
elif op == 3 :
    print('Essa forma de pagamento não possui desconto, portanto o preço do produto será de R${:.2f}'.format(valor_normal))
else :
    valor_com_juros = valor_normal * 1.20
    print('Essa forma de pagamento pussui um juros de 20%, portanto o preço do produto com juros será de R${:.2f}'.format(valor_com_juros))