'''Elabore um algoritmo que leia um número de entrada
que indicará a quantidade de números a serem lidos.
Em seguida, leia n números inteiros e positivos, e ao final, imprima o maior número digitado.
'''

quantidade = int(input("Informe a quantidade de números a serem lidos: "))
maior = 0
for i in range(1,quantidade+1):
    numero = int(input(f"Informe o {i}° número: "))
    if(numero > maior):
        maior = numero
print(f"O maior número digitado foi {maior}")