#Enunciado: Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).

contador = soma = 0

while True:

    num = int(input('Digite um número inteiro: '))

    if num == 999:
        break 
    else:
        soma += num
        contador += 1

print()
print('Soma = {}'.format(soma))
print('Quantidade de números digitados: {}'.format(contador))