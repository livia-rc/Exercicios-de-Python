from lib.interface import *
from lib.arquivo import *
from pathlib import Path

arquivo = Path(__file__).parent / 'Arquivo.txt'

if not arquivoExiste(arquivo):
    criarArquivo(arquivo)

while True: 
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do Sistema'])
    if resposta == 1:
        #opção de listar o conteúdo do arquivo
        lerArquivo(arquivo)
    elif resposta == 2:
        #Opção para cadastrar novas pessoas 
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrarPessoa(arquivo, nome, idade)
    elif resposta == 3:
        print('Encerrando o programa...')
        break
    else:
        print('\033[31mOpção Inválida! Tente novamente\033[m')