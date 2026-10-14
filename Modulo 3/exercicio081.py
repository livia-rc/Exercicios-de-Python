#Enunciado: Crie um programa que vai ler vários números e colocar em uma lista.Depois disso mostre:                                                                                                                          A) Quantos números foram   digitados.                                                                                                                    
#B) A lista de valores, ordenada de forma decrescente.                                                                                          
#C) Se o valor 5 foi digitado e está ou não na lista.

lista = []
cont = 1
while True:
    valor = int(input('Digite o {}° valor: '.format(cont)))

    while valor in lista:
        print('Esse valor não pode ser adicionado pois já existe na lista. Tente novamente!\n')
        valor = int(input('Digite outro valor: '))
    
    lista.append(valor)
    print('Valor adicionado!\n')

    cont += 1
    op = str(input('Deseja adicionar mais um valor (SIM ou NÃO)? ')).upper()

    if op == 'NAO' or op == 'NÃO':
        print('Programa encerrado!')
        break

print('\nQuantidade de números digitados: {}'.format(len(lista)))
lista.sort(reverse=True)
print('Lista em ordem decrescente: {}'.format(lista))

if 5 in lista:
    print('O número 5 foi digitado e está na lista!')
else:
    print('O número 5 não foi digitado!')