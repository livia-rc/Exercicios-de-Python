#Enunciado: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario_atual = float(input('Digite seu sálario atual: R$'))

salario_reajustado = salario_atual * 1.15

print('Seu sálario após o aumento de 15% passou a ser R${:.2f}' .format(salario_reajustado))