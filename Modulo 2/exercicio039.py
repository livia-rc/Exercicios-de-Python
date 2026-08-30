#Enunciado: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
ano_nascimento = int(input('Digite o ano que você nasceu: '))

ano_atual = date.today().year

idade = ano_atual - ano_nascimento

if idade < 18:
    saldo = 18 - idade
    print('Você tem {} anos e vai se alistar daqui há {} anos.'.format(idade, saldo))
elif idade == 18:
    print('Você tem {} anos e está na hora de se alistar'.format(idade))
else:
    saldo = idade - 18
    print('Você tem {} anos e já deveria ter se alistado há {} anos'.format(idade, saldo))