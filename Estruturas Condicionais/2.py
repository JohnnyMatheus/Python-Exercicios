'''Desenvolva um algoritmo que classifique um número de entrada fornecido pelo usuário como PAR ou ÍMPAR.'''

numero = int(input('Informe um numero: '))

if(numero % 2 == 0):
    print(f"O numero {numero} é PAR")
else:
    print(f"O numero {numero} é ÍMPAR")
