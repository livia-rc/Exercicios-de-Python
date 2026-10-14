#Enunciado: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

lista_numeros = []
lista_pares = []
lista_impares = []

for n in range(0, 7):
    num = int(input('Digite o {}° valor: '.format(n+1)))
    lista_numeros.append(num, )

for n in lista_numeros:
    if n % 2 == 0:
        lista_pares.append(n)
    else:
        lista_impares.append(n)

print('\nLista dos números digitados:')
for n in lista_numeros:
    print('{}'.format(n), end=', ')

print('\n\nLista dos números pares em ordem crescente:')
for p in sorted(lista_pares):
    print('{}'.format(p), end=', ')

print('\n\nLista dos números ímpares em ordem crescente:')
for i in sorted(lista_impares):
    print('{}'.format(i), end=', ')