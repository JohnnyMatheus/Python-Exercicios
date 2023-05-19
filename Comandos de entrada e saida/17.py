'''Elabore um algoritmo que leia três números reais, num1, num2 e num3 e
imprima o valor de y, sabendo-se que:

y = num1 + num2/    + 2*(num1- num2)
         num3+num1
'''

num1 = float(input("Informe o 1° número: "))
num2 = float(input("Informe o 2° número: "))
num3 = float(input("Informe o 3° número: "))

y = num1 + (num2/(num3+num1)) + (2*(num1-num2))
print(y)