#Enunciado: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

quantidade = int(input('Quantos valores você deseja inserir na lista? '))

lista = []
for n in range(0, quantidade):
    valor = int(input('Digite o {}° valor que você deseja inserir: '.format(n + 1)))

    while valor in lista:
        print('Esse valor não pode ser adicionado pois já existe na lista. Tente novamente!\n')
        valor = int(input('Digite o {}° valor que você deseja inserir: '.format(n + 1)))

    lista.append(valor)
    print('Valor adicionado!\n')

lista.sort()
print('Os valores únicos digitados, em ordem crescente, são:')
print(lista)