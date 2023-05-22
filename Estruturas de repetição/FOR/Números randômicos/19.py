'''Escrever um programa que gere 1 número randômico entre 1 e 100
e mostre os números contidos nesse intervalo.
Por exemplo, se for sorteado o número 5, deve mostrar os números
do 1 até o 5.  Mostar 10 números por linha.
'''
import random
linha = 10
contador = 0
X = random.randint(1,100)
print(X)

for i in range(X +1):
    print(i,end=" ")
    contador +=1
    if(contador == linha):
        print()
        contador =0
print()