def aumentar(v, a):
    total = v + a
    return total



def diminuir(v, d):
    total = v - d
    return total



def dobro(v):
    valor_dobrado = v * 2
    return valor_dobrado




def metade(v):
    metade_valor = v / 2
    return metade_valor


def moeda(preco):
    return f'R${preco:.2f}'.replace('.', ',') #.replace('.', ',') substitui o ponto decimal por uma vírgula, seguindo o padrão monetário brasileiro.