#Enunciado: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

a = int(input('Digite o comprimento da primeira reta: '))
b = int(input('Digite o comprimento da segunda reta: '))
c = int(input('Digite o comprimento da terceira reta: '))

if a < b + c and b < a + c and c < a + b:
    print('Essas retas podem formar um triângulo!')
else:
    print('Essas retas não podem formar um triângulo!')