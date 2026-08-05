#Enunciado: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

num = int(input('Digite um número inteiro: '))
op = int(input('Escolha qual será a base de conversão:\n1) Binário\n2) Octal\n3) Hexadecimal\nOpção: '))

if op == 1:
    print('O número {} convertido para binário é igual a {}'.format(num, bin(num)[2:]))
elif op == 2:
    print('O número {} convertido para octal é igual a {}'.format(num, oct(num)[2:]))
elif op == 3:
    print('O número {} convertido para hexadecimal é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida! Tente novamente')