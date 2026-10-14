#Enunciado: Aprimore o desafio anterior, mostrando no final:                                                    
# A) A soma de todos os valores pares digitados.                                                                                                  
# B) A soma dos valores da terceira coluna.                                                                                                                
# C) O maior valor da segunda linha.


matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = soma2 = 0

for lin in range(0, 3):
    for col in range(0, 3):
        matriz[lin][col] = int(input('Digite um valor para a posição {} {}: '.format(lin, col)))

print()

for lin in range(0, 3):
    for col in range(0, 3):
        print(f'[{matriz[lin][col]:^5}]', end='')
    print()

for lin in range(0, 3):
    for col in range(0, 3):
        if matriz[lin][col] % 2 == 0:
            soma += matriz[lin][col]

for lin in range(0, 3):
    soma2 +=  matriz [lin][2]

for col in range(0, 3):
    if col == 0:
        maior = matriz[1][0]
    else:
        if matriz[1][col] > maior:
            maior = matriz[1][col]

print()

print('A soma de todos os valores pares digitados é igual a {}'.format(soma))
print('A soma dos valores da terceira coluna é igual a {}'.format(soma2))
print('O maior valor da segunda linha é igual a {}'.format(maior))