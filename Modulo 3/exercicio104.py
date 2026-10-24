#Enunciado: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)

def leiaInt(msg):
    while True: # o programa continua perguntando até receber um valor válido
        num = input(msg) #exibe a msg e recebe o que o usuário digitou

        if num.isdigit(): #verifica se há apenas dígitos
            return int(num)
        else:
            print('ERRO! Digite um número inteiro válido.')


# Programa principal
n = leiaInt('Digite um n: ')
print(f'Você digitou o número {n}.')
