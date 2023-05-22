'''Construa um programa que sorteie 50 números inteiros entre 0 e 500
e no final informe quantas vezes o valor 100 foi sorteado.'''
import random
vezes =0
for i in range(50):
    numero = random.randint(0,500)
    print(numero)
    if(numero == 100):
        vezes +=1
print(vezes)
