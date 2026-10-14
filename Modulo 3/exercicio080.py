#Enunciado: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

lista = []

for v in range(0, 5):
    valor = int(input('Digite o {}° valor: '.format(v + 1)))

    if v == 0:
        lista.append(valor)  #Adiciona o primeiro valor diretamente na lista
    else:
        pos = 0  #Começa a procurar a posição correta a partir do início da lista

        #Percorre a lista enquanto houver posições e o valor digitado for maior que o valor encontrado na posição atual
        while pos < len(lista) and valor > lista[pos]:
            pos += 1  #Avança para a próxima posição

        #Insere o valor na posição encontrada, mantendo a lista ordenada
        lista.insert(pos, valor)

print('\nLista ordenada:')
print(lista)