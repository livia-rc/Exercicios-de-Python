#Enunciado: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

def voto(ano_nascimento):
    from datetime import datetime

    ano_atual = datetime.today().year
    idade = ano_atual - ano_nascimento

    if idade < 16:
        return (f'Você tem {idade} anos, portanto ainda não pode votar')
    elif idade >= 16 and idade < 18:
        return (f'Você tem {idade} anos, portanto seu voto é opcional')
    else:
        return (f'Você tem {idade} anos, portanto seu voto é obrigatório')



#programa principal
ano_nascimento = int(input('Digite seu ano de nascimento: '))
print(voto(ano_nascimento))