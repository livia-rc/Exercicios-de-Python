#Enunciado: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.

primeiro_termo = int(input('Digite o primeiro termo da Progressão Aritmética: '))
razao = int(input('Digite o valor da razão da Progressão Aritmética: '))
n = int(input('Quantos termos dessa PA você deseja visualizar? '))

print('\nOs {} primeiros termos dessa PA são:\n'.format(n))

termo_n = 0
c = 1
op = 1

while op != 0: 
    while c < n + 1:
        termo_n = primeiro_termo + ((c - 1) * razao)
        c += 1
        print('{}° termo = {}'.format(c - 1, termo_n))
    print('\nVocê deseja ver o {}° termo dessa PA?'.format(c))
    op = int(input('[1] SIM\n[0] NÃO\nEscolha uma opção: '))
    print()

    if op == 1:
        termo_n = primeiro_termo + ((c - 1) * razao)
        c += 1
        print('{}° termo = {}'.format(c - 1, termo_n))
    else:
        break
