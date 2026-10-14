produtos = ['Livro', 'Caneta', 'Borracha', 'Estojo', 'Lápis', 'Post-It', 'Planner', 'Caderno'] #listas são mutáveis
print(produtos)
print(produtos[3])
print('Esta lista possui {} produtos'.format(len(produtos)))

produtos[3] = 'Mochila'
print(produtos)
print(produtos[3])
print('Esta lista possui {} produtos'.format(len(produtos)))

produtos.append('Agenda') #inserir no final da lista
print(produtos)
print('Esta lista possui {} produtos'.format(len(produtos)))

produtos.insert(2, 'Corretivo') #inserir em uma posição específica
print(produtos)
print('Esta lista possui {} produtos'.format(len(produtos)))

produtos.pop() #remover o ultimo elemento da lista
print(produtos)
print('Esta lista possui {} produtos'.format(len(produtos)))

produtos.pop(2) #remover o elemento da posição 2 da lista
print(produtos)
print('Esta lista possui {} produtos'.format(len(produtos)))

valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Fim da lista!')

valores2 = []
for cont in range(0, 5):
    valores2.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores2):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Fim da lista!')