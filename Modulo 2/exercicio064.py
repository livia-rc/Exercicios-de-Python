#Enunciado: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

parada = 0
soma = 0
contador = 0

while parada != 999:

    num = int(input('Digite um número: '))

    if num != 999:
        soma += num
        contador += 1

    parada = num

print('A quantidade de números digitados foi igual a {} e a soma deles é {}'.format(contador, soma))