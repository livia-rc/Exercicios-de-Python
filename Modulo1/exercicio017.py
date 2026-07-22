#Enunciado: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa. hip² = co² + ca²

import math
cateto_oposto = float(input('Digite o valor do cateto oposto do triângulo: '))

cateto_adjacente = float(input('Digite o valor do cateto adjacente do triângulo: '))

hipotenusa = math.sqrt(math.pow(cateto_oposto, 2) + math.pow(cateto_adjacente, 2)) #ou math.hypot(cateto_oposto, cateto_adjacente)

print('O valor da hipotenusa de um triângulo retângulo com cateto oposto igual a {:.2f} e cateto adjacente igual a {:.2f} é igual a {:.2f}' .format(cateto_oposto, cateto_adjacente, hipotenusa))
