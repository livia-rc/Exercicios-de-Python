#Enunciado: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

lista_numeros = []

for n in range(0, 5):
    lista_numeros.append(int(input('Digite o {}° número: '.format(n+1))))

print('\nA lista gerada com esses números é:')
print(lista_numeros)


for n in range(0, len(lista_numeros)):
    if n == 0:
        maior = lista_numeros[0]
        menor = lista_numeros[0]
        pos_maior = 0 
        pos_menor = 0
    else:
        if lista_numeros[n] > maior:
            maior = lista_numeros[n]
            pos_maior = n

        if lista_numeros[n] < menor:
            menor = lista_numeros[n]
            pos_menor = n

print('O maior valor digitado é {} e está na posição {}'.format(maior, pos_maior+1))
print('O menor valor digitado é {} e está na posição {}'.format(menor, pos_menor+1))