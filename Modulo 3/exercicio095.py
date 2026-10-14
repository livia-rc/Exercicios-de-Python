#Enunciado: Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

#Enunciado do exercício 93: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

jogadores = {}
time = []
cont = 1

while True:
    jogadores['Nome'] = str(input(f'Digite o nome do {cont}° jogador: '))
    jogadores['Quantidade de Partidas'] = int(input(f'Digite a quantidade de partidas que o {jogadores["Nome"]} jogou: '))

    gols = []

    print('Digite a quantidade de gols feitos em cada partida: ')
    for c in range(0, jogadores['Quantidade de Partidas']):
        gol = int(input(f'{c+1}° Partida: '))
        gols.append(gol)

    jogadores['Gols por Partida'] = gols
    jogadores['Total de Gols'] = sum(gols)

    time.append(jogadores.copy())

    op = str(input('Deseja adicionar mais um jogador (SIM ou NÃO)? ')).upper()

    if op == 'NAO' or op == 'NÃO':
        print('Programa Encerrado!')
        break

    print()
    cont += 1

print()
for k, v in enumerate(time):
    print(f'{k+1}° Jogador: ')
    print(f'Nome: {v["Nome"]}\nQuantidade de Partidas: {v["Quantidade de Partidas"]}\nGols por Partida: {v["Gols por Partida"]}\nTotal de Gols: {v["Total de Gols"]}\n')