'''Elabore um algoritmo que leia números inteiros enquanto os valores informados forem
positivos ou zero.  Quando um número negativo for
informado devem ser mostrados quantos números que foram digitados (incluindo o último número).'''
contador =0
numero = 0
while numero >= 0:
    contador +=1
    numero = int(input("Informe um numero inteiro ou numero negativo para sair: "))
print(f"Numeros digitados: {contador}")