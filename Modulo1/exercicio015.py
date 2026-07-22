import math #importamos todas as funções da biblioteca math
#ou podemos fazer assim para importar apenas a função sqrt: from math import sqrt

num = int(input('Digite um número: '))
raiz = math.sqrt(num)

print('A raiz de {} é igual a {}' .format(num, raiz))
