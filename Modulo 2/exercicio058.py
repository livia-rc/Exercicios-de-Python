#Enunciado: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

import random

numero = int(input('Tente adivinhar o número pensado pelo computador! Escolha um número de 0 a 10: '))

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
escolhido = random.choice(lista) #faz o programa sortear um numero entre 0 e 10 de forma aleatoria
contador = 1

while numero != escolhido:
    numero = int(input('O computador não escolheu este número, tente novamente! Escolha um número entre 0 e 10: '))
    contador += 1

print('Parabéns você adivinhou! O número era {} e você precisou de {} tentativas para acertar'.format(escolhido, contador))
