'''Modifique o programa anterior para mostrar também o menor valor gerado.'''

import random

numero = random.randint(1,10)
print("Numero aleatório escolhido foi: ",numero)
maior = 0
menor = 0
for i in range(numero+1):
    print(i)
    if(numero > maior):
        maior = numero
    if (numero < menor):
        menor = numero
print(f'O maior número = {maior}')
print(f"O menor número = {menor}")