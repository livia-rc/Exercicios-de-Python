#Enunciado: Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu

import random

numero = int(input('Tente adivinhar o número pensado pelo computador! Escolha um número de 0 a 5: '))

lista = [0, 1, 2, 3, 4, 5]
escolhido = random.choice(lista) #faz o programa sortear um numero entre 0 e 5 de forma aleatoria

if numero == escolhido:
    print('Parabéns você adivinhou o número pensado!')
else:
    print('Que pena, você errou!\nO número era: {}'.format(escolhido))