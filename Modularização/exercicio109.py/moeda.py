def aumentar(v, a, format=False):
    total = v + a
    return total if format is False else moeda(total)



def diminuir(v, d, format=False):
    total = v - d
    return total if format is False else moeda(total)



def dobro(v, format=False):
    valor_dobrado = v * 2
    return valor_dobrado if format is False else moeda(valor_dobrado)




def metade(v, format=False):
    metade_valor = v / 2
    return metade_valor if format is False else moeda(metade_valor)


def moeda(preco):
    return f'R${preco:.2f}'.replace('.', ',') #.replace('.', ',') substitui o ponto decimal por uma vírgula, seguindo o padrão monetário brasileiro.