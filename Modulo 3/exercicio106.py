
c = (
    '\033[m',           # 0 - Sem cor
    '\033[0;30;41m',    # 1 - Preto com fundo vermelho
    '\033[0;30;42m',    # 2 - Preto com fundo verde
    '\033[0;30;43m',    # 3 - Preto com fundo amarelo
    '\033[0;30;44m',    # 4 - Preto com fundo azul
    '\033[0;30;45m',    # 5 - Preto com fundo roxo
    '\033[0;30;46m',    # 6 - Preto com fundo ciano
    '\033[0;30;47m',    # 7 - Preto com fundo branco
    '\033[0;97;40m'     # 8 - Branco com fundo preto
)


def ajuda(com):
    print(c[4], end='')
    help(com)
    print(c[0], end='')


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('-' * tam)
    print(f'  {msg}')
    print('-' * tam)
    print(c[0], end='')


# Programa principal
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    comando = input('Função ou Biblioteca > ')

    if comando.upper() == 'FIM':
        break

    ajuda(comando)

titulo('ATÉ LOGO', 5)
