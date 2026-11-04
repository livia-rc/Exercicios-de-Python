try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except Exception as erro:
    print(f'Infelizmente tivemos um problema!O problema encontrado foi {erro.__class__}')
else:
    print(f'O resultado da divisão é {r}')
finally:
    print('Volte sempre! Muito obrigado')