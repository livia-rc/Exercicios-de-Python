def mostraLinha(): #usamos o comando def para criar uma função
    print('-'*30)

mostraLinha()
print('CADASTRO DE FUNCIONÁRIOS')
mostraLinha()

def mensagem(msg): #msg é um parametro
    print('-'*30)
    print(msg)
    print('-' *30)

mensagem('SOMA DE VALORES')

def soma(a, b):
    s = a + b
    print(f'a = {a}\nb = {b}\nSoma = {s}')
    


soma(4, 5)
soma(8, 9)
soma(a=2, b=1) 


#empacotar parametros
def contador(*num): # * = desempacotar (nos da mais liberdade para adicionar quantos parametros quiser)
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números')


contador(2, 1, 7)
contador(4, 9, 3, 6, 8, 5)


def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1


valores = [7, 2, 5, 4]
print(valores)
dobra(valores)
print(valores)