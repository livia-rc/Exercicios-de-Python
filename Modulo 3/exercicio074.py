#Enunciado: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint

valor = (randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))

print('Números gerados: {}, {}, {}, {}, {}'.format(valor[0], valor[1], valor[2], valor[3], valor[4]))

for c in range(len(valor)):
    if c == 0:
        maior = valor[0]
        menor = valor[0]
    else:
        if valor[c] >= maior:
            maior = valor[c]
        
        if valor[c] < menor:
            menor = valor[c]

print('Maior valor = {}'.format(maior))
print('Menor valor = {}'.format(menor))