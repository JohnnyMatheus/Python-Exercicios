'''Construir um programa para mostrar a tabuada de um número inteiro informado pelo usuário.
Por exemplo, se for informado o valor 5 teremos:
5 x 0   =    0
5 x 1   =    5
5 x 2   =   10
5 x 3   =   15
5 x 4   =   20
5 x 5   =   25
5 x 6   =   30
5 x 7   =   35
5 x 8   =   40
5 x 9   =   45
5 x 10 =    50
'''

numero = int(input("Informe um número: "))
for i in range(11):
   print(f"{numero} X {i} = {numero*i}")