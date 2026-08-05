#Enunciado: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math

angulo = float(input('Digite o valor do ângulo: '))

angulo_radianos = math.radians(angulo)
seno = math.sin(angulo_radianos)
cosseno = math.cos(angulo_radianos)
tangente = math.tan(angulo_radianos)

print('O ângulo {:.2f} possui:\nSeno = {:.2f}\nCosseno = {:.2f}\nTangente = {:.2f}' .format(angulo, seno, cosseno, tangente))