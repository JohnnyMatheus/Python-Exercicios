'''Elabore um algoritmo que leia um número inteiro e informe se ele é divisível por 5, por 3 e por 2.'''

numero = int(input("Informe um  número: "))

if(numero % 5 == 0) and (numero % 3 == 0) and (numero % 2 ==0):
    print(f"O número {numero} é divisivel por 5, 3 e 2")
else:
    print("Não é divisível por 5,3 e 2")
