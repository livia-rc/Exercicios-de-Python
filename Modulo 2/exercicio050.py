#Enunciado: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

soma = 0

for cont in range(1, 7):
    num = int(input('Digite o {}° número: '.format(cont)))
    if num % 2 == 0:
        soma += num

print('A soma dos números pares digitados é igual a {}'.format(soma))