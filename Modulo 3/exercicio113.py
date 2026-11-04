#Enunciado: Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

def leiaInt(msg):
    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! O número digitado não é um inteiro válido\033[m')
        else:
            return num 



def leiaFloat(msg):
    while True:
        try:
            num = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! O número digitado não é um real válido\033[m')
        else:
            return num 



#principal
n = leiaInt('Digite um número: ')
print(f'Você digitou o número {n}.')

f = leiaFloat('Digite um número: ')
print(f'Você digitou o número {f}.')
