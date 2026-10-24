#Enunciado: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

def maior(*numeros): #O asterisco antes do parâmetro permite que a função receba vários argumentos
    maior_valor = numeros[0] #considera o primeiro número como o maior inicialmente.

    for valor in numeros: #percorre todos os números recebidos.
        if valor > maior_valor: #verifica se o número atual é maior que o maior encontrado até aquele momento.
            maior_valor = valor #valor atualiza o maior valor quando encontra um número superior.
    print(f'O maior valor contido nessa lista é o número {maior_valor}')



lista_valores = []
contador = 0

while True:
    contador += 1
    valor = int(input(f'Digite o {contador}° valor que será adicionado na lista: '))
    lista_valores.append(valor)

    op = str(input('Você deseja adicionar mais um valor na lista (SIM ou NÃO)? ')).upper()

    if op == 'NÃO' or op == 'NAO':
        print('Encerrando programa!')
        break

print(lista_valores)
maior(*lista_valores)