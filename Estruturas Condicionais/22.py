'''Construir um algoritmo que, tome como entrada três valores diferentes
e os imprima em ordem decrescente.'''



valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))
valor3 = float(input("Digite o terceiro valor: "))


if valor1 >= valor2 and valor1 >= valor3:
    if valor2 >= valor3:
        print("Valores em ordem decrescente:", valor1, valor2, valor3)
    else:
        print("Valores em ordem decrescente:", valor1, valor3, valor2)
elif valor2 >= valor1 and valor2 >= valor3:
    if valor1 >= valor3:
        print("Valores em ordem decrescente:", valor2, valor1, valor3)
    else:
        print("Valores em ordem decrescente:", valor2, valor3, valor1)
else:
    if valor1 >= valor2:
        print("Valores em ordem decrescente:", valor3, valor1, valor2)
    else:
        print("Valores em ordem decrescente:", valor3, valor2, valor1)
