'''Elabore um algoritmo que leia um número e imprima uma das mensagens: é múltiplo de 3, ou, não é
múltiplo de 3.'''

numero = int(input("Informe um número: "))

if(numero % 3 == 0):
    print(f"O número {numero} é multiplo de 3")
else:
    print(f"O número {numero} não é multiplo de 3")