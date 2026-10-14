#Enunciado: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

lista_alunos = []
cont = 0

while True:

    cont += 1
    aluno = str(input('Digite o nome do {}° aluno: '.format(cont)))
    nota1 = float(input('Digite a primeira nota desse aluno: '))
    nota2 = float(input('Digite a segunda nota desse aluno: '))

    media = (nota1 + nota2)/2

    lista_alunos.append((aluno, nota1, nota2, media) )

    op = str(input('\nVocê deseja adicionar mais um aluno (SIM ou NÃO)? ')).upper()
    print()

    if op == 'NÃO' or op == 'NAO':
        print('\nPrograma encerrado!\n')
        break

print('-' * 5, f' BOLETIM DE {cont} ALUNOS', '-' * 5)
for i, a in enumerate(lista_alunos):
    print('\n{}° aluno(a)'.format(i+1))
    print('Nome: {}'.format(a[0]))
    print('Média: {}'.format(a[3]))

while True:
    op = str(input('\nVocê deseja ver as notas de algum aluno específico (SIM ou NÃO)? ')).upper()

    if op == 'NÃO' or op == 'NAO':
        print('\nPrograma encerrado!')
        break

    indice = int(input('\nDigite o número da aluno no boletim: '))

    if 1 <= indice <= len(lista_alunos):
        aluno = lista_alunos[indice - 1]
        print('\nNome: {}'.format(aluno[0]))
        print('1° Nota: {}'.format(aluno[1]))
        print('2° Nota: {}'.format(aluno[2]))
    else:
        print('\nAluno não encontrado!')
