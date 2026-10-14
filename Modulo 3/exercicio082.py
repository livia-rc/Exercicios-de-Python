#Enunciado: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

lista = []
lista_pares = []
lista_impares = []
cont = 1

while True:
    num = int(input('Digite o {}° número: '.format(cont)))

    if num not in lista:
        lista.append(num)
        print('Número adicionado na lista!\n')
    else:
        while num in lista:
            print('Este número já foi adicionado, tente novamente!')
            num = int(input('Digite outro número: '))
        lista.append(num)
        print('Número adicionado na lista!\n')
    
    cont += 1

    op = str(input('Deseja adicionar mais um valor (SIM ou NÃO)? ')).upper()
    
    if op == 'NAO' or op == 'NÃO':
        print('Programa encerrado!')
        break

for n in range(len(lista)):
    if lista[n] % 2 == 0:
        num_par = lista[n]
        lista_pares.append(num_par)
    else:
        num_impar = lista[n]
        lista_impares.append(num_impar)

print('Lista gerada:')
print(lista)
print('Lista dos números pares:')
print(lista_pares)
print('Lista dos números ímpares:')
print(lista_impares)