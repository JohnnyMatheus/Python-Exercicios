'''Considere um algoritmo que calcule a área de uma circunferência, dada por área = π X RAIO2.'''
import math
Raio = float(input("Informe o valor do raio: "))
area = math.pi * Raio**2
print("A área da circunferência é: {:.2f}".format(area))