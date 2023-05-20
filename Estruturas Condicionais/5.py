'''Elabore um algoritmo que leia o nome e o peso de duas pessoas e imprima os dados da pessoa mais pesada.
Os pesos delas serão diferentes.'''

nome1 = str(input("Informe o nome da 1° pessoa: "))
peso1 = float(input("Informe o peso da 1° pessoa: "))
nome2 = str(input("Informe o nome da 2° pessoa: "))
peso2 = float(input("Informe o peso da 2° pessoa: "))

if(peso1 > peso2):
    print(f"{nome1} é mais pesado")
elif(peso2 > peso1):
    print(f"{nome2} é mais pesado")
elif(peso1 == peso2):
    print("Mesmo peso")
else:
    print("Algo deu errado.Tente novamente")
