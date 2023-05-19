'''
Escrever um programa que calcule a quantidade de tinta necessária para pintar uma parede retangular,
considerando que cada litro de tinta é suficiente para pintar 5 m2 de parede.
'''

base = float(input("Informe a largura da parede: "))
altura = float(input("Informe a altura da parede: "))
litro = 5
qtdTinta = (base * altura)/litro
print(f"A quantidade de tinta necessária para pintar uma parede retangular será de {qtdTinta} litros")