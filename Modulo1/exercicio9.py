#Enunciado: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

real = float(input('Digite o valor em reais que você tem na carteira: R$'))

dolar = real / 5.09

print('Com R${:.2f} você pode comprar US${:.2f}' .format(real, dolar))
