#Enunciado: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

from random import randint
def sorteia(lista):
    for n in range(0, 5):
        num = randint(1, 10)
        lista.append(num)



def somaPar(lista):
    somatorio = 0
    for i in range(len(lista)):
        if lista[i] % 2 == 0:
            somatorio += lista[i]
    return somatorio
        

#Principal
numeros = []

sorteia(numeros)

print('Números sorteados:')
print(numeros)

somaTotal = somaPar(numeros)
print(f'A soma dos números pares contidos nessa lista é igual a {somaTotal}')