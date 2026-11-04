#Enunciado: Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado.

import moeda

valor = float(input('Digite um valor em R$: '))

print()
aumento = float(input('Digite o valor do aumento em R$: '))
total_com_aumento = moeda.aumentar(valor, aumento)
print(f'O valor depois do aumento é de {moeda.moeda(total_com_aumento)}')

print()
desconto = float(input('Digite o valor do desconto em R$: '))
total_com_desconto = moeda.diminuir(valor, desconto)
print(f'O valor depois do desconto é de {moeda.moeda(total_com_desconto)}')

print()
dobro = moeda.dobro(valor)
print(f'O dobro de {moeda.moeda(valor)} é {moeda.moeda(dobro)}')

print()
metade = moeda.metade(valor)
print(f'A metade de {moeda.moeda(valor)} é {moeda.moeda(metade)}')