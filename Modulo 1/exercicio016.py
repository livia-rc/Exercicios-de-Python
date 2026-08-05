#Enunciado: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
import math

num = float(input('Digite um número real: '))
parte_inteira = math.trunc(num)

print('O valor digitado foi {} e sua parte inteira é {}' .format(num, parte_inteira))