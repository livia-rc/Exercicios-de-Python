#Enunciado: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date
ano_atual = date.today().year
contador_maiores = 0
contador_menores = 0

for pessoa in range(1, 8):
    ano_nasc = int(input('Digite o ano de nascimento da {}° pessoa: '.format(pessoa)))
    idade = ano_atual - ano_nasc

    if idade >= 18:
        contador_maiores += 1
    else:
        contador_menores += 1

print('{} pessoas são maiores de idade'.format(contador_maiores))
print('{} pessoas são menores de idade'.format(contador_menores))
