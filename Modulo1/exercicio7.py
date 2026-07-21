#Enunciado: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

n = float(input('Digite um valor em metros: '))

centimetros = n * 100
milimetros = n * 1000

print('O valor de {:.2f}m corresponde a {:.0f}cm e {:.0f}mm' .format(n, centimetros, milimetros))