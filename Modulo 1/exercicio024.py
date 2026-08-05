#Enunciado: Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

nome_completo = str(input('Digite seu nome completo: ')).strip()

print('Seu nome tem Silva? {}'.format('SILVA' in nome_completo.upper()))