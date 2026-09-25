#Enunciado: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

import random 

escolha = str(input('Escolha par ou ímpar: ')).upper()

resultado = escolha_comp = ''
soma = contador = 0

if escolha == 'PAR':
    escolha_comp = 'ÍMPAR'
else:
    escolha_comp = 'PAR'

while True:
    num_jogador = int(input('Digite um número entre 1 e 5: '))
    num_comp = random.randint(1,5)

    soma = num_jogador + num_comp

    if soma % 2 == 0:
        resultado = 'PAR'
    else:
        resultado = 'ÍMPAR'

    print('Você jogou {} e o computador jogou {} a soma entre esses valores é {} que é um número {}'.format(num_jogador, num_comp, soma, resultado))

    if resultado == escolha:
        contador += 1
        print('\nVocê venceu! Vamos jogar novamente\n')
    else:
        print('\nVocê perdeu! Jogo encerrado\n')
        break

print('Você venceu {} vezes consecutivas'.format(contador))