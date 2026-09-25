#Enunciado: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

primeiro_termo = int(input('Digite o primeiro termo da Progressão Aritmética: '))
razao = int(input('Digite o valor da razão da Progressão Aritmética: '))

print('\nOs 10 primeiros termos dessa PA são:\n')

termo_n = 0
n = 1

while n < 11:
    termo_n = primeiro_termo + ((n - 1) * razao)
    n += 1
    print('{}° termo = {}'.format(n - 1, termo_n))