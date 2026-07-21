#Enunciado: Crie um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

n = input('Digite algo: ')
print('O tipo primitivo desse valor é', type(n)) #type() é uma função que retorna o tipo do valor
print('Só tem espaços?', n.isspace()) #isspace() verifica se o valor é composto apenas por espaços
print('É um número?', n.isnumeric()) #isnumeric() verifica se o valor é composto apenas por números
print('É alfabético?', n.isalpha()) #isalpha() verifica se o valor é composto apenas por letras
print('É alfanumérico?', n.isalnum()) #isalnum() verifica se o valor é composto apenas por letras e números
print('Está em maiúsculas?', n.isupper()) #isupper() verifica se o valor está em maiúsculas
print('Está em minúsculas?', n.islower()) #islower() verifica se o valor está em minúsculas
print('Está capitalizado?', n.istitle()) #istitle() verifica se o valor está capitalizado (primeira letra maiúscula e as demais minúsculas)