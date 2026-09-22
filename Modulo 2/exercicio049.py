#Enunciado: Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for

num = int(input('Digite o número que você deseja verificar a tabuada: '))

print('\n\nTabuada do número {}:'.format(num))

for multiplicador in range(1, 11):
    resultado = num * multiplicador
    print('{} x {} = {}'.format(num, multiplicador, resultado))