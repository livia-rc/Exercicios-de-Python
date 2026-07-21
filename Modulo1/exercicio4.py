#Enunciado: Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.

n = int(input('Digite um número: '))

sucessor = n + 1
antecessor = n - 1

print('O antecessor de {} é {} e o sucessor é {}' .format(n, antecessor, sucessor))