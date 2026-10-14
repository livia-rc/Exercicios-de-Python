#Enunciado: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre: 
#A) Quantas pessoas foram cadastradas.
#B) Uma listagem com as pessoas mais pesadas.
#C) Uma listagem com as pessoas mais leves.

lista_pessoas = []
lista_dados = []
lista_maisPesados = []
lista_maisLeves = []

cont = 1

while True:
    nome = str(input('Digite o nome da pessoa que será cadastrada: '))
    lista_dados.append(nome)

    peso = float(input('Digite o peso em kg da pessoa que será cadastrada: '))
    lista_dados.append(peso)

    lista_pessoas.append(lista_dados[:])
    lista_dados.clear()

    op = str(input('\nDeseja cadastrar mais uma pessoa (SIM ou NÃO)? ')).upper()
    print()

    if op == 'NÃO' or op == 'NAO':
        print('Programa encerrado!\n')
        break


print('{} pessoas foram cadastradas!\n'.format(len(lista_pessoas)))

print('Pessoas cadastradas:\n')

for p in lista_pessoas:
    print('{}° Pessoa:\nNome: {}\nPeso: {:.2f}kg\n'.format(cont, p[0], p[1]))
    cont += 1


# Descobre o maior e o menor peso
for n in range(len(lista_pessoas)):
    if n == 0:
        maior_peso = lista_pessoas[n][1]
        menor_peso = lista_pessoas[n][1]
    else:
        if lista_pessoas[n][1] > maior_peso:
            maior_peso = lista_pessoas[n][1]

        if lista_pessoas[n][1] < menor_peso:
            menor_peso = lista_pessoas[n][1]


# Separa as pessoas mais pesadas e mais leves
for p in lista_pessoas:
    if p[1] == maior_peso:
        lista_maisPesados.append(p)

    if p[1] == menor_peso:
        lista_maisLeves.append(p)


print('Pessoas mais leves:')

for pl in lista_maisLeves:
    print('Nome: {}\nPeso: {:.2f}kg\n'.format(pl[0], pl[1]))


print('Pessoas mais pesadas:')

for pp in lista_maisPesados:
    print('Nome: {}\nPeso: {:.2f}kg\n'.format(pp[0], pp[1]))