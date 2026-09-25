#Enunciado: Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.

print('Vamos fazer algumas operações entre dois valores')
valor1 = float(input('Digite o primeiro valor: '))
valor2 = float(input('Digite o segundo valor: '))
print('----- MENU -----\n[1] Soma\n[2] Multiplicação\n[3] Compara maior valor\n[4] Digitar novos números\n[5] Sair')
op = int(input('Escolha uma opção do menu: '))

soma = 0
multiplicacao = 0

while op != 5:
    if op == 1:
        soma = valor1 + valor2
        print('{:.2f} + {:.2f} = {:.2f}'.format(valor1, valor2, soma))
        print('\n----- MENU -----\n[1] Soma\n[2] Multiplicação\n[3] Compara maior valor\n[4] Digitar novos números\n[5] Sair')
        op = int(input('Escolha uma opção do menu: '))

    elif op == 2:
        multiplicacao = valor1 * valor2
        print('{:.2f} x {:.2f} = {:.2f}'.format(valor1, valor2, multiplicacao))
        print('\n----- MENU -----\n[1] Soma\n[2] Multiplicação\n[3] Compara maior valor\n[4] Digitar novos números\n[5] Sair')
        op = int(input('Escolha uma opção do menu: '))

    elif op == 3:
        if valor1 > valor2:
            print('O primeiro valor digitado é maior! ({} > {})'.format(valor1, valor2))
        elif valor2 == valor1:
            print('Os valores digitados são iguais! ({} = {})'.format(valor1, valor2))
        else:
            print('O segundo valor digitado é maior! ({} > {})'.format(valor2, valor1))
        print('\n----- MENU -----\n[1] Soma\n[2] Multiplicação\n[3] Compara maior valor\n[4] Digitar novos números\n[5] Sair')
        op = int(input('Escolha uma opção do menu: '))
        
    elif op == 4:
        print('Digite novos valores!')
        valor1 = float(input('Digite o primeiro valor: '))
        valor2 = float(input('Digite o segundo valor: '))
        print('\n----- MENU -----\n[1] Soma\n[2] Multiplicação\n[3] Compara maior valor\n[4] Digitar novos números\n[5] Sair')
        op = int(input('Escolha uma opção do menu: '))

    else:
        print('Valor inválido!')
        print('\n----- MENU -----\n[1] Soma\n[2] Multiplicação\n[3] Compara maior valor\n[4] Digitar novos números\n[5] Sair')
        op = int(input('Escolha uma opção do menu: '))