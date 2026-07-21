#Enunciado: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n = int(input('Digite um número inteiro: '))

dobro = n * 2
triplo = n * 3
raiz_quadrada = n ** (1/2) #ou raiz_quadrada = pow(n, 1/2)

print('\nResultados para o número {}: \nDobro: {} \nTriplo: {} \nRaiz Quadrada: {:.2f}' .format(n, dobro, triplo, raiz_quadrada)) 
#{:.2f} é uma formatação que limita o número de casas decimais para 2