nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))

media = (nota1 + nota2)/2

print('Média = {:.1f}' .format(media))

if media >= 7.0:
    print('Parabéns, você foi aprovado!')
else:
    print('Você foi reprovado :(')

# outra forma de usar condições (forma simplificada)
# print('Aprovado!' if media >= 7.0 else 'Reprovado!')