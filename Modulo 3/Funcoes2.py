def contador(i, f, p):
    """
    Faz uma contagem e mostra na tela
    i = inicio da contagem
    f = fim da contagem
    p = passo
    return = sem retorno
    """
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('FIM')


help(contador)

def somar(a, b, c=0): # c é um parametro opcional
    s = a + b + c
    print(f'Soma = {s}')

somar(2, 3, 6)
somar(5, 2)

def teste():
    x = 8 #variavel local
    print(f'Na função teste x vale {x}')

#principal
x = 10 #variavel global
print(f'No programa principal x vale {x}')
teste()