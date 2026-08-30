#Enunciado: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#– EQUILÁTERO: todos os lados iguais
#– ISÓSCELES: dois lados iguais, um diferente
#– ESCALENO: todos os lados diferentes

a = int(input('Digite o comprimento da primeira reta: '))
b = int(input('Digite o comprimento da segunda reta: '))
c = int(input('Digite o comprimento da terceira reta: '))

if a < b + c and b < a + c and c < a + b:
    if a == b and b == c:
        print('Essas retas podem formar um triângulo equilátero!')
    elif a == b or a == c or b ==c:
        print('Essas retas podem formar um triângulo isóceles!')
    else:
        print('Essas retas podem formar um triângulo escaleno!')
else:
    print('Essas retas não podem formar um triângulo!')