'''Elabore um algoritmo que leia dois números inteiros e efetue a sua adição.
Caso a soma seja maior ou igual a 10, mostre a soma na tela,
caso contrário informe que a soma é menor que dez.'''

numero1 = int(input("Informe 1° número: "))
numero2 = int(input("Informe 2° número: "))
soma = numero1 + numero2

if(soma >=10):
    print(f"A soma entre {numero1} + {numero2} = {soma}")
else:
    print("A soma é menor que 10")