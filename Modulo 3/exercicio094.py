#Enunciado: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: A) Quantas pessoas foram cadastradas B) A média de idade C) Uma lista com as mulheres D) Uma lista de pessoas com idade acima da média

dados = {}
pessoas = []
mulheres = []
mais_velhos = []

print('=' * 20)
print('CADASTRO DE PESSOAS')
print('=' * 20)

while True:
    dados['Nome'] = str(input('Digite o nome completo: '))
    dados['Idade'] = int(input('Digite a idade: '))
    dados['Sexo'] = str(input('Digite o sexo (homem ou mulher): ')).upper()
    if dados['Sexo'] != 'HOMEM' and dados['Sexo'] != 'MULHER':
        print('Erro! Sexo inválido')
        continue
    pessoas.append(dados.copy())

    op = str(input('\nDeseja cadastrar mais uma pessoa (Sim ou Não)? ')).upper()
    print()

    if op == 'NÃO' or op == 'NAO':
        print('\nPROGRAMA ENCERRADO!\n')
        break

soma = 0
for i in pessoas:
    soma += i['Idade']

media = soma / len(pessoas)

for m in pessoas:
        if m['Sexo'] == 'MULHER':
            mulheres.append(m)

for i in pessoas:
    if i['Idade'] >= media:
         mais_velhos.append(i)

print('Total de pessoas cadastradas: {}'.format(len(pessoas)))
print('A média da idade das pessoas cadastradas é {} anos'.format(media))
print('Total de mulheres cadastradas: {}'.format(len(mulheres)))
print('Quantidade de pessoas com idade acima da média: {}'.format(len(mais_velhos)))

print()
print('=' * 25)
print('PESSOAS CADASTRADAS')
print('=' * 25)
for k, v in enumerate(pessoas):
    print(f'\n{k+1}° Pessoa:\nNome: {v["Nome"]}\nIdade: {v["Idade"]}\nSexo: {v["Sexo"]}')