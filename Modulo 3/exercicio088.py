#Enunciado: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta

from random import randint

quant = int(input('Quantos jogos você quer que eu gere? '))
lista = []
jogos = []
tot = 1

while tot <= quant:
    cont  = 0
    while True:
        n = randint(1, 60)
        if n not in lista:
            lista.append(n)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1

print('-' * 5, f' SORTEANDO {quant} JOGOS', '-' * 5)

for i, l in enumerate(jogos):
    print('Jogo {}: {}'.format(i+1, l))