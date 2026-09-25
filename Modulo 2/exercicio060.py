#Enunciado: Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120

num = int(input('Digite um número inteiro: '))

fatorial = 1
temp = num

while temp != 0:
    fatorial *= temp
    temp -= 1

print('{}! = {}'.format(num, fatorial))