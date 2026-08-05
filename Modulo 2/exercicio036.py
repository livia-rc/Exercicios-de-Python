#Enunciado: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

valor_casa = float(input('Qual é o valor da casa? R$'))
salario_comprador = float(input('Qual é o seu salário em reais? R$'))
anos = int(input('Em quantos anos você irá pagar? '))

prestacao_mensal = valor_casa / (anos * 12)

print('A prestação mensal desse empréstimo é de R${:.2f}'.format(prestacao_mensal))

if prestacao_mensal > 0.30 * salario_comprador:
    print('Empréstimo negado!')
else:
    print('Empréstimo confirmado!')