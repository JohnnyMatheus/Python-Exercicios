'''Elabore um algoritmo que leia dois números inteiros e imprima qual é maior, qual é menor,
ou se os dois números são iguais.'''

num1 = int(input("Informe o 1° número: "))
num2 = int(input("Informe o 2° número: "))

if(num1 > num2):
    print(f"O Número {num1} é maior que {num2}")
elif(num2 > num1):
    print(f"O Número {num2} é maior que {num1}")
else:
    print(f"São Iguais {num1} = {num2}")