#Enunciado: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão

primeiro_termo = int(input('Digite o primeiro termo da Progressão Aritmética: '))
razao = int(input('Digite o valor da razão da Progressão Aritmética: '))

print('\nOs 10 primeiros termos dessa PA são:\n')
for n in range(1, 11):
    termo_n = primeiro_termo + ((n - 1) * razao)
    print('{}° termo = {}'.format(n, termo_n))
