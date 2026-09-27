#Enunciado: Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

palavras = ('Menina', 'Camisa', 'Motocicleta', 'Carro', 'Uva', 'Paisagem')

for p in palavras:
    print('\nNa palavra {} temos '.format(p.upper()), end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')