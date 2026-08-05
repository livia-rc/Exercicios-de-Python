#Enunciado: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

largura = float(input('Digite a largura da parede em metros: '))
altura = float(input('Digite a altura da parede em metros: '))

area = largura * altura

quantidade_necessaria = area / 2

print('Para pintar uma parede de {:.2f}m² de área serão necessários {:.2f}L de tinta' .format(area, quantidade_necessaria))