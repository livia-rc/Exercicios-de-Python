#Enunciado: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

op = 'SIM'
soma = 0
contador = 0

while op != 'NÃO':
    num = int(input('Digite um número inteiro: '))
    soma += num

    contador += 1

    if contador == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num


    op = str(input('Você deseja continuar digitando números (SIM ou NÃO)? ')).upper()

media = soma/contador
print('A média entre os valores digitados é igual a {}'.format(media))
print('O maior valor digitado é {}'.format(maior))
print('O menor valor digitado é {}'.format(menor))