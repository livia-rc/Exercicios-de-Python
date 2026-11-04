def aumentar(v, a, format=False):
    total = v + (v * (a/100))
    return total if format is False else moeda(total)



def diminuir(v, d, format=False):
    total = v - (v * (d/100))
    return total if format is False else moeda(total)



def dobro(v, format=False):
    valor_dobrado = v * 2
    return valor_dobrado if format is False else moeda(valor_dobrado)




def metade(v, format=False):
    metade_valor = v / 2
    return metade_valor if format is False else moeda(metade_valor)


def moeda(preco):
    return f'R${preco:.2f}'.replace('.', ',') #.replace('.', ',') substitui o ponto decimal por uma vírgula, seguindo o padrão monetário brasileiro.

def resumo(preco=0, taxa_aumento=10, taxa_reducao=5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: {moeda(preco)}')
    print(f'Dobro do Preço: {dobro(preco, True)}')
    print(f'Metade do Preço: {metade(preco, True)}')
    print(f'Valor com Acréscimo de {taxa_aumento}%: {aumentar(preco, taxa_aumento, True)}')
    print(f'Valor com Desconto de {taxa_reducao}%: {diminuir(preco, taxa_reducao, True)}')
    print('-' * 30)
