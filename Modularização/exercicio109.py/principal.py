#Enunciado: Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado. Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando.

import moeda

valor = float(input('Digite um valor em R$: '))

print()
aumento = float(input('Digite o valor do aumento em R$: '))
total_com_aumento = moeda.aumentar(valor, aumento, True)
print(f'O valor depois do aumento é de {total_com_aumento}')

print()
desconto = float(input('Digite o valor do desconto em R$: '))
total_com_desconto = moeda.diminuir(valor, desconto, True)
print(f'O valor depois do desconto é de {total_com_desconto}')

print()
dobro = moeda.dobro(valor, True)
print(f'O dobro de {moeda.moeda(valor)} é {dobro}')

print()
metade = moeda.metade(valor, True)
print(f'A metade de {moeda.moeda(valor)} é {metade}')