#Enunciado: Crie um programa que leia o nome completo de uma pessoa e mostre:
#– O nome com todas as letras maiúsculas e minúsculas.
#– Quantas letras ao todo (sem considerar espaços).
#– Quantas letras tem o primeiro nome.

nome_completo = str(input('Digite seu nome completo: ')).strip()
print('Seu nome em maiúsculas é: {}' .format(nome_completo.upper()))
print('Seu nome em minúsculas é: {}' .format(nome_completo.lower()))
print('Seu nome possui ao todo {} letras' .format(len(nome_completo) - nome_completo.count(' ')))
print('Seu primeiro nome possui {} letras' .format(nome_completo.find(' '))) #contar as letras do primeiro nome, find() retorna a posição do primeiro espaço, que é a quantidade de letras do primeiro nome

#len = comprimento da String
#count = contar a quantidade de uma variavel
#in = x in y (existe x na string y ? retorna true ou false)
#replace = substituir
#upper = transformar para maiusculas
#lower = transformar para minusculas
#capitalize = transformar apenas o primeiro caractere da string para maiuscula
#title = transformar a primeira letra de cada palavra da string para maiuscula
#strip = remover os espaços inuteis do inicio e do fim da string
#rstrip = remover apenas os espaços inuteis da direita
#lstrip = remover apenas os espaços inuteis da esquerda
#split = dividir a string considerando os espaços que formará uma lista de strings
#join = juntar strings