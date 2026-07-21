#Enunciado: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit. Considerando a fórmula (0 °C × 9/5) + 32

temperatura_graus_Celsius = float(input('Digite a temperatura em graus Celsius (°C): '))

temperatura_graus_Fahrenheit = (temperatura_graus_Celsius * 9/5) + 32

print('A temperatura de {:.2f}°C coreesponde a {:.2f}°F' .format(temperatura_graus_Celsius, temperatura_graus_Fahrenheit))