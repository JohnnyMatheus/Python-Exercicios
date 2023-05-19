'''Elabore um algoritmo que leia uma temperatura em graus centígrados e apresente-a
convertida em graus Fahrenheit. A fórmula de conversão é:F = 9/5 * C + 32'''
#F é a temperatura em Fahrenheit e C é a temperatura em graus centígrados ou Celsius.

C = float(input("Informe a temperatura em °C a ser convertida: "))
F = 9/5 * C + 32
print(f"A temperatura em {C}°C convertida para °F:{F} graus Fahrenheit  ")
