#Enunciado: Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500

soma = 0
for num in range(1, 501):
    if num % 3 == 0:
        print('{}'.format(num), end=' ')
        soma += num

print('\nA soma de todos os valores múltiplos de três no intervalo entre 1 e 500 é igual a {}'.format(soma))