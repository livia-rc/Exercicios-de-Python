#Enunciado: Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.


def fatorial(n, show=False):
    num = n
    fat = 1

    while n >= 1:
        if show:
            print(n, end='')
            if n > 1:
                print(' x ', end='')

        fat *= n
        n -= 1

    if show:
        print(f' = {fat}')

    return f'O fatorial de {num} é {fat}'


# Programa principal
print(fatorial(8, False))
print()
print(fatorial(5, True))
