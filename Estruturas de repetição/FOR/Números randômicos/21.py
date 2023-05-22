'''Escrever um programa que gere e mostre 10 números aleatórios (randômicos) entre 50 e 100.
Em seguida mostre qual foi o maior valor gerado.
Note que nesse exercício o maior valor possível será 100 e o menor valor possível será 50. '''
import random

numero = random.randint(1,10)
print("Numero aleatório escolhido foi: ",numero)
maior = 0
for i in range(50,100):
    print(i)
    if(numero > maior):
        maior = numero
print(f"O maior numero foi {maior}")

