#Enunciado: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os números pares.

valores = ()
par = 0 #contador
pares = ()

for v in range(0, 4):
    valor = int(input('Digite um valor entre 1 e 10: '))
    valores += (valor,)

print()
for v in range(len(valores)):
    print('{}° Valor: {}'.format(v+1, valores[v]))

for v in range(len(valores)):
    if valores[v] % 2 == 0:
        par += 1
        pares += (valores[v],)

print()

if 9 in valores:
    print('O valor 9 apareceu {} vez(es)'.format(valores.count(9)))
else:
    print('O valor 9 não foi digitado!')

if 3 in valores:
    print('O valor 3 apareceu na posição {}'.format(valores.index(3)+1))
else: 
    print('O valor 3 não foi digitado!')

if par >= 1:
    print('Há {} números pares'.format(par), pares[0:])
else:
    print('Não há números pares!')
