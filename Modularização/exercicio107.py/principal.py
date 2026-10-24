#Enunciado: Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.

import moeda

valor = float(input('Digite um valor em R$: '))

print()
aumento = float(input('Digite o valor do aumento em R$: '))
total_com_aumento = moeda.aumentar(valor, aumento)
print('O valor depois do aumento é de R${:.2f}'.format(total_com_aumento))

print()
desconto = float(input('Digite o valor do desconto em R$: '))
total_com_desconto = moeda.diminuir(valor, desconto)
print('O valor depois do desconto é de R${:.2f}'.format(total_com_desconto))

print()
dobro = moeda.dobro(valor)
print('O dobro de R${:.2f} é R${:.2f}'.format(valor, dobro))

print()
metade = moeda.metade(valor)
print('A metade de R${:.2f} é R${:.2f}'.format(valor, metade))
