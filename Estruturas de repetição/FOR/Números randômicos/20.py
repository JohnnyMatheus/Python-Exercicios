'''Escrever um programa que gere 20 números aleatórios (randômicos) entre 0 e 100
e conte quantos desses são pares e quantos são impares.'''
import random
par = 0
impar = 0
numero = random.randint(20,100)
print(numero)

for i in range(numero):
    print(i)
    if(i % 2 == 0):
       par +=1
    else:
       impar +=1

print(f"Números Pares: {par}\n"
      f"Números Impares : {impar}")
