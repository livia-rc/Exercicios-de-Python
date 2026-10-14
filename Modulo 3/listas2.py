pessoas = [
    ['Pedro', 25],
    ['Maria', 19],
    ['João', 32]
]

print(pessoas) #printar a lista toda
print(pessoas[1]) #vai mostrar toda a lista que esta na posição 1 da lista pessoas
print(pessoas[0][0]) #pessoa na posição 0 item na posição 0

for p in pessoas:
    print('Nome: {}\nIdade: {} anos'.format(p[0], p[1]))

galera = []
dado = []
totmaior = totmenor = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

print(galera)
for p in galera:
    if p[1] >= 18:
        print('{} é maior de idade'.format(p[0]))
        totmaior += 1 
    else:
        print('{} é menor de idade'.format(p[0]))
        totmenor += 1
print('Temos {} maiores e {} menores de idade'.format(totmaior, totmenor))
aluno = []
turma = []
aluno.append('Gustavo')
aluno.append('12')
turma.append(aluno)
print(turma)