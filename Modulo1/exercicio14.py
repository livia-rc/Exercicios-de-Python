#Enunciado: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km_percorridos = float(input('Digite a quantidade de quilometros (km) percorridos pelo carro: '))
dias_aluguel = int(input('Digite a quantidade de dias pelos quais o carro foi alugado: '))

preço_total = (60 * dias_aluguel) + (0.15 * km_percorridos)

print('O valor final do aluguel do carro foi de R${:.2f}' .format(preço_total))