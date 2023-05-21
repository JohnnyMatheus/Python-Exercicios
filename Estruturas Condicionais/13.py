'''Elabore um algoritmo para ler três valores e verificar se eles podem ser os comprimentos dos lados de um triângulo,
e se forem, dizer o tipo de triângulo.

Para ser um triângulo é necessário que qualquer um dos lados seja menor que a soma dos outros dois lados.
(A < B+C) (B < A+C) (C < A+B).

Para verificar qual o tipo de triângulo, seguimos as seguintes regras:

Equilátero é aquele que tem os três lados iguais. (A = B = C)
Isósceles é aquele que tem dois lados iguais. (A = B ) ou  (A = C) ou  (B = C)
Escaleno é aquele que tem todos os lados diferentes (A  ≠ B ≠ C)
'''

ladoA = float(input("Informe o valor do 1° lado: "))
ladoB = float(input("Informe o valor do 2° lado: "))
ladoC = float(input("Informe o valor do 3° lado: "))

if(ladoA < ladoB + ladoC) and (ladoB < ladoA + ladoC) and (ladoC < ladoA + ladoB):
    print("É um triângulo:")
    if(ladoA == ladoB == ladoC):
        print("Equilátero")
    elif(ladoA == ladoB) or (ladoA == ladoC) or (ladoB == ladoC):
        print("Isóceles")
    else:
        print("Escaleno")
else:
    print("Não forma um Triângulo")


