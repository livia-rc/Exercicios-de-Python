#Enunciado: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.

multiplicacao = 0 

num = int(input('Digite o número que você deseja ver a tabuada: '))

while True:

    if num < 0:
            print('\nPrograma Encerrado!')
            break
    
    print('\n----- TABUADA DO {} -----'.format(num))
    for c in range(1, 11):
        multiplicacao = num * c
        print('{} x {} = {}'.format(num, c, multiplicacao))

    print()

    print('Se quiser encerrar o programa digite um número negativo!')
    num = int(input('Digite o número que você deseja ver a tabuada: '))
    
