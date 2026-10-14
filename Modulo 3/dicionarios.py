# dados = []
# dados.append('Jana')
# dados.append(23)
# print(dados[0])
# print(dados[1])

# dados = {'nome':'Jana', 'idade':23}
# print(dados['nome'])

# dados['sexo'] = 'M'
# del dados['idade']

# filme = {'titulo':'Star Wars',
#          'ano':1977,
#          'diretor':'George Lucas'}

# print(filme.values())
# print(filme.keys())
# print(filme.items())

# for k, v in filme.items():
#     print(f'O {k} é {v}')


pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(f'O {pessoas["nome"]} te {pessoas["idade"]} anos')

print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

for k, v in pessoas.items():
    print(f'{k} = {v}')

pessoas['nome'] = 'leandro'
pessoas['peso'] = 87

for k, v in pessoas.items():
    print(f'{k} = {v}')

Brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
Brasil.append(estado1)
Brasil.append(estado2)

print(Brasil)

estado = {}
brasil = []
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}')