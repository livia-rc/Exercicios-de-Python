#Enunciado: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

soma_idades = 0
homem_maior = 0
nome_homem_maior = ''
contador = 0

for pessoa in range(1, 5):
    print('----- Dados da {}° pessoa -----'.format(pessoa))
    nome = str(input('Digite seu nome: '))
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo biológico (Homem ou Mulher): ')).lower()
    print()

    soma_idades += idade

    if sexo == 'homem':
        if idade > homem_maior:
            homem_maior = idade
            nome_homem_maior = nome

    if sexo == 'mulher':
        if idade < 20:
            contador += 1

media_idades = soma_idades/4

print('A média das idades do grupo é igual a {}'.format(media_idades))
print('A idade do homem mais velho é igual a {} anos e seu nome é {}'.format(homem_maior, nome_homem_maior))
print('{} mulheres possuem menos de 20 anos'.format(contador))