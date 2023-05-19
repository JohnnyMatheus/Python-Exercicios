'''
Escrever um algoritmo que solicite ao usuário dois números inteiros (n1 e n2).
Em seguida calcule e apresente os seguintes resultados:
a.Média aritmética dos dois valores
b.Diferença entre os dois valores
c.Soma dos dois valores
'''

n1 = int(input("Informe o 1° número: "))
n2 = int(input("Informe o 2° número: "))
media = (n1 + n2)/2
diferenca = n1 - n2
soma = n1 + n2
print(f"A media entre {n1} e {n2} = {media}\nA diferença entre {n1} - {n2} = {diferenca}\nA soma entre {n1} + {n2} = {soma}")
