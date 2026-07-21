#Enunciado: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preço_original = float(input('Digite o preço original de um produto: R$'))

preço_com_desconto = preço_original * 0.95

print('O preço do produto após ser aplicado um desconto de 5% é igual a R${:.2f}' .format(preço_com_desconto))