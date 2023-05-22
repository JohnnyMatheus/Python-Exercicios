'''Elabore um algoritmo que leia 20 números inteiros.
Ao final deve ser informado quantos maiores que 10 foram lidos e a sua média.'''
cont = 0
for i in range(1,21):
    numero = int(input(f"Informe o {i}° número: "))
    if(numero > 10):
     cont +=1
print(f"Foram lidos {cont} numeros maiores que 10")
