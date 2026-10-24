#Enunciado: Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def area(largura, comprimento):
    areaTotal = largura * comprimento
    print('A área do terreno é {:.2f}m²'.format(areaTotal))


largura = float(input('Digite a largura, em metros, do terreno: '))
comprimento = float(input('Digite o comprimento, em metros, do terreno: '))

area(largura, comprimento)
