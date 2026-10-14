#Enunciado: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

dados = {}

dados['Nome'] = str(input('Digite o nome do jogador: '))
dados['Quantidade de Partidas'] = int(input(f'Digite a quantidade de partidas que o {dados["Nome"]} jogou: '))

gols = []
print('Digite a quantidade de gols feitos em cada partida')
for c in range(0, dados['Quantidade de Partidas']):
    gol = int(input(f'{c+1}° Partida: '))
    gols.append(gol)

dados['Gols por Partida'] = gols
dados['Total de Gols'] = sum(gols)

for i, v in dados.items():
    print(f'{i}: {v}')