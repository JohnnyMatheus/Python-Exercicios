'''Construir um programa para ler 20 números inteiros e encontrar o maior valor informado
(considere que todos são positivos, maiores que zero).'''
maior = 0
for i in range(1,5+1):
    numero = int(input(f"Informe o {i}° número: "))
    if(numero >maior):
        maior = numero

print(f"O maior valor informado foi {maior}")
