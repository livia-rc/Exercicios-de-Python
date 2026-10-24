#Enunciado: Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.


def ficha(nome='', gols=0):
    print('-=' * 20)
    print('FICHA DO JOGADOR')
    print('-=' * 20)

    if nome:
        print(f'Nome: {nome}')
    else:
        print('Nome não informado!')

    print(f'Quantidade de gols: {gols}')


# Programa principal
nome = input('Digite o nome do jogador: ')
gols = input('Digite a quantidade de gols marcados por este jogador: ')

if gols.isdigit():
    gols = int(gols)
else:
    gols = 0

ficha(nome, gols)
