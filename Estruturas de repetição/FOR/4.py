'''Elabore um algoritmo que leia um número de entrada que indicará a quantidade de números a serem lidos.
Em seguida, leia n números (conforme o valor informado anteriormente) e imprima o triplo de cada um.'''

quantidade = int(input("Informe a quantidade de números a serem lidos: "))
for i in range(1,quantidade+1):
    numero = int(input(f"Informe o {i}° número: "))
    calc = numero * 3
    print(f"O triplo de {numero} é =  {calc}")
