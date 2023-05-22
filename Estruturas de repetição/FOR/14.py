'''Elabore um algoritmo que leia 200 números, e imprima quantos são pares e quantos são ímpares.'''

par = 0
impar = 0
for i in range(1,201):
    if(i % 2 == 0):
        par +=1
    else:
        impar +=1
print(f"Números Pares = {par}\n"
      f"Números impares = {impar}")