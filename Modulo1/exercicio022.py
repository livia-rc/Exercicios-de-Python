#Enunciado:  Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

numero = int(input('Digite um número de 0 a 9999: '))
unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10
print('Os dígitos separados do número {} são:\nUnidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}' .format(numero, unidade, dezena, centena, milhar))