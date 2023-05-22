'''
Elabore um algoritmo que leia um número e imprima todos os números de 1 até o número lido,
 e no final mostre também o produto de todo os números. Exemplo:

Número: 3			Saída: 1 2 3 	Produto: 6'''

numero = int(input("Informe a quantidade de números a serem lidos: "))
soma = 0
for i in range(1,numero +1):
    print(i)
    soma = soma + i
print("Produto = ",soma)
