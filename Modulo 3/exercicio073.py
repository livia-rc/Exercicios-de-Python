#Enunciado: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
#a) Os 5 primeiros times.
#b) Os últimos 4 colocados.
#c) Times em ordem alfabética.
#d) Em que posição está o time da Chapecoense.

times = ('Flamengo', 'Palmeiras', 'Athletico-PR', 'Fluminense', 'Bahia', 'Cruzeiro', 'Atlético-MG', 'Santos', 'Coritiba', 'Bragantino', 'São Paulo', 'Botafogo', 'EC Vitória', 'Corinthians', 'Mirassol', 'Vasco da Gama', 'Grêmio', 'Internacional', 'Remo', 'Chapecoense')

print('=' * 50)
print('{:^50}'.format('TABELA DO CAMPEONATO BRASILEIRO'))
print('=' * 50)

print('\n5 PRIMEIROS COLOCADOS:')
for t in range(0, len(times)):
    if t <= 4:
        print('{}° {}'.format(t+1, times[t]))

print('\n4 ÚLTIMOS COLOCADOS:')
for t in range(0, len(times)):
    if t >=16:
        print('{}° {}'.format(t+1, times[t]))

print('\nTIMES EM ORDEM ALFABÉTICA:')
for time in sorted(times):
    print(time)

print('\nPOSIÇÃO DA CHAPECOENSE:')
print('{}° Posição'.format(times.index('Chapecoense')+1))