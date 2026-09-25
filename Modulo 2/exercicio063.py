#Enunciado: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo: 0 – 1 – 1 – 2 – 3 – 5 – 8

n = int(input('Digite quantos primeiros termos da sequência de Fibonacci você deseja visualizar: '))

primeiro_termo = 0
segundo_termo = 1
c = 2

if n == 1:
    print('1° termo = {}'.format(primeiro_termo))

elif n >= 2:
    print('1° termo = {}'.format(primeiro_termo))
    print('2° termo = {}'.format(segundo_termo))

    while c < n:
        n_termos = primeiro_termo + segundo_termo

        primeiro_termo = segundo_termo
        segundo_termo = n_termos

        c += 1

        print('{}° termo = {}'.format(c, n_termos))