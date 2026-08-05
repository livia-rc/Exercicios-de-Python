#Enunciado: Faça um programa que leia dois números e mostre a soma, subtração, multiplicação, divisão, potência, divisão inteira e módulo entre eles.

n1 = float(input('Digite o primeiro número: ')) 
n2 = float(input('Digite o segundo número: '))

soma = n1 + n2
subtracao = n1 - n2
multiplicacao = n1 * n2
divisao = n1 / n2
potencia = n1 ** n2
divisao_inteira = n1 // n2
modulo = n1 % n2

print('\nResultados das operações entre {} e {}: \n' .format(n1, n2))
print('Soma: {}' .format(soma))
print('Subtração: {}' .format(subtracao))
print('Multiplicação: {}' .format(multiplicacao))
print('Divisão: {}' .format(divisao))
print('Potência: {}' .format(potencia))
print('Divisão inteira: {}' .format(divisao_inteira))
print('Módulo: {}' .format(modulo))

#Operações aritméticas
# + adição
# - subtração
# * multiplicação
# / divisão
# ** potência
# // divisão inteira
# % módulo (resto da divisão)

#Ordem de precedência
# 1º - ()
# 2º - **
# 3º - * / // %
# 4º - + -