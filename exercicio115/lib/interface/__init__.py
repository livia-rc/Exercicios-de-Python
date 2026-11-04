def linha(tam = 42):
    return ('-' * tam)


def cabecalho(texto):
    print(linha())
    print(texto.center(42))
    print(linha())

def leiaInt(msg):
    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! O número digitado não é um inteiro válido\033[m')
        else:
            return num 


        
def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c} \033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    op = leiaInt('\033[32mEscolha uma opção: \033[m')
    return op