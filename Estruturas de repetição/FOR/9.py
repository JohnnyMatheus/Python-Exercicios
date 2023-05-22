'''Elabore um algoritmo que leia 10 números, e imprima quantos números maiores
 ou iguais a 20 foram digitados.'''
''''''
maior = 0
for i in range(1,11):
    Numero = int(input(f"Informe o {i}° número: "))
    if(Numero >=20):
        maior +=1
print("Quantidade de números maiores ou iguais a 20:", maior)

