lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim') #tuplas são imutáveis
#hambúrguer está na posição [0]
#Suco está na posição [1]
#Pizza está na posição [2]
#Pudim está na posição [3]
print(lanche[1])
print(lanche[0:]) #da posição 0 até o final da tupla
print(lanche[0:2]) #da posição 0 até a posição 2 mas sem mostrar a posição 2

print(len(lanche)) #printar o tamanho da tupla 
for comida in lanche:
    print('Eu vou comer {}'.format(comida))

#for comida in range(0, len(lanche)):
#   print('Eu vou comer {}'.format(comida))

print(sorted(lanche)) #mostrar em ordem

a = (2, 5, 4, 8)
b = (1, 3, 6, 7)
c = a + b #concatenar
print(c) 
print(c.count(3)) #quantidade de vezes que o elemento aparece
print(sorted(c))
print(c.index(8)) #mostra o indice que o elemento aparece
