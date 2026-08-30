#Enunciado: Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint
print('Vamos jogar Jokenpô com o computador!\n')
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

print('Opções de jogada\n0. Pedra\n1. Papel\n2. Tesoura')
jogador = int(input('Escolha uma opção: '))

print('O computador escolheu {}'.format(itens[computador]))
print('O jogador escolheu {}'.format(itens[jogador]))

if computador == 0 : #computador jogou pedra
    if jogador == 0 :
        print('EMPATE!')
    elif jogador == 1 :
        print('JOGADOR GANHOU!')
    else :
        print('COMPUTADOR GANHOU!')
elif computador == 1: #computador jogou papel
    if jogador == 0 :
        print('COMPUTADOR GANHOU!')
    elif jogador == 1 :
        print('EMPATE!')
    else :
        print('JOGADOR GANHOU!')
elif computador == 2: #computador jogou tesoura
    if jogador == 0:
        print('JOGADOR GANHOU!')
    elif jogador == 1:
        print('COMPUTADOR GANHOU!')
    else :
        print('EMPATE!')