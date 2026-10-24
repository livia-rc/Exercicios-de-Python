#Enunciado: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
#Quantidade de notas
#A maior nota
#A menor nota
#A média da turma
#A situação(opcional)

def notas(*nota, situacao=False):
    r = {}
    r['Total'] = len(nota)
    r['Maior'] = max(nota)
    r['Menor'] = min(nota)
    r['Média'] = sum(nota)/len(nota)

    if situacao:
        if r['Média'] >= 7:
            r['Situação'] = 'BOA'
        elif r['Média'] >= 5 and  r['Média'] < 7:
            r['Situação'] = 'RAZOÁVEL'
        else:
            r['Situação'] = 'RUIM'
    return r



#programa principal
resp = notas(9, 10, 5.5, 3, situacao=True)
print(resp)
