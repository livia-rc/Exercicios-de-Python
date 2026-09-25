#Enunciado: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
#A) quantas pessoas tem mais de 18 anos.
#B) quantos homens foram cadastrados.
#C) quantas mulheres tem menos de 20 anos.

parada = 'NÃO'
contador_idade = contador_homens = contador_mulheres_menores_20 = 0

while True:
    nome = str(input('Digite seu nome: '))
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo biológico (homem ou mulher): ')).upper()

    if idade > 18:
        contador_idade += 1

    if sexo == 'HOMEM':
        contador_homens += 1
    else:
        if idade < 20:
            contador_mulheres_menores_20 += 1

    op = str(input('\nVocê deseja cadastrar mais uma pessoa (SIM ou NÃO): \n')).upper()

    if op == parada:
        print('\nForam cadastrados:\n{} pessoas com mais de 18 anos\n{} homens\n{} mulheres com menos de 20 anos'.format(contador_idade, contador_homens, contador_mulheres_menores_20))
        print('\nPrograma encerrado!')
        break