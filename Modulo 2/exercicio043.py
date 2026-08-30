#Enunciado: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
#– IMC abaixo de 18,5: Abaixo do Peso
#– Entre 18,5 e 25: Peso Ideal
#– 25 até 30: Sobrepeso
#– 30 até 40: Obesidade
#– Acima de 40: Obesidade Mórbida

peso = float(input('Digite seu peso em kg: '))
altura = float(input('Digite sua altura em m: '))

valor_imc = peso/ (altura * altura)

print('Seu IMC é igual a {:.2f}, portanto sua classificação é: '.format(valor_imc))

if valor_imc < 18.5:
    print('ABAIXO DO PESO!')
elif valor_imc >= 18.5 and valor_imc < 25:
    print('PESO IDEAL!')
elif valor_imc >= 25 and valor_imc < 30:
    print('SOBREPESO!')
elif valor_imc >= 30 and valor_imc < 40:
    print('OBESIDADE!')
else:
    print('OBESIDADE MÓRBIDA!')