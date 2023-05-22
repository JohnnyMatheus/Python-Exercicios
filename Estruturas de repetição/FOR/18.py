'''Elabore um algoritmo que leia um número de entrada
n que indicará a quantidade de números a serem lidos.
Em seguida, leia n números (conforme o valor informado anteriormente)
e, ao final imprima o menor número digitado. Note que nesse caso não sabemos
o intervalo dos valores possíveis, assim vamos usar outra informação:
o maior número que pode ser armazenado em uma variável em Python é ‘inf’,
portanto, se esse é o maior número possível, qualquer número será menor que ele.'''

quantidade = int(input("Informe a quantidade de números a serem lidos: "))
menor = float('inf')
for i in range(1,quantidade+1):
    numero = int(input(f"Informe o {i}° número: "))
    if(numero < menor):
        menor = numero
print(f"O menor número lido foi {menor}")
